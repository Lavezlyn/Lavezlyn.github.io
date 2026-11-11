# -*- coding: utf-8 -*-
"""Build the compact homepage after Jekyll; content remains in _pages and _bibliography.

Usage: python3 bin/build_homepage.py [--output PATH]
Run after Jekyll for a complete site, or alone for a homepage-only preview.
Preview with: python3 -m http.server --directory PATH 8765
Edit _pages/about.md, _pages/about_zh.md, _bibliography/papers.bib, and
assets/homepage/{style.css,app.js}; publication images live in
assets/img/publication_preview/. Keep .github/workflows/deploy.yml in sync.
"""
from pathlib import Path
from hashlib import sha256
import re, html, shutil
import argparse
import yaml
SRC = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description='Build the approved bilingual homepage into a Jekyll output directory.')
parser.add_argument('--output', type=Path, default=SRC / '_site')
OUT = parser.parse_args().output.resolve()
OUT.mkdir(parents=True, exist_ok=True)
stylesheet_version = sha256((SRC / 'assets/homepage/style.css').read_bytes()).hexdigest()[:12]
shutil.copytree(SRC / 'assets/homepage', OUT / 'assets/homepage', dirs_exist_ok=True)
for name in ('prof_pic.png', 'favicon.png'):
    shutil.copy2(SRC / 'assets/img' / name, OUT / 'assets/homepage' / name)
for name in ('CNAME', '.nojekyll'):
    if (SRC / name).exists():
        shutil.copy2(SRC / name, OUT / name)

def esc(s):
    return html.escape(s)

def md(s):
    s = re.sub('\\[([^]]+)\\]\\(([^)]+)\\)', '<a href="\\2">\\1</a>', s)
    s = re.sub('\\*\\*(.+?)\\*\\*', '<strong>\\1</strong>', s)
    s = re.sub('_(.+?)_', '<em>\\1</em>', s)
    return s
papers = []
for raw in re.split('\\n(?=@)', (SRC / '_bibliography/papers.bib').read_text()):
    fields = dict(re.findall('^\\s*(\\w+)\\s*=\\s*\\{(.*?)\\},?\\s*$', raw, re.M))
    fields['key'] = re.search('@\\w+\\{([^,]+)', raw)[1]
    fields['raw'] = raw.strip()
    papers.append(fields)
    if 'preview' in fields:
        image = SRC / 'assets/img/publication_preview' / fields['preview']
        shutil.copy2(image, OUT / 'assets/homepage' / fields['preview'])
short = {'fang2026truthful': 'Introducing TruthfulVQA and an inverse scaling law: slower multimodal reasoning is not always more truthful.', 'fang2026debate': 'Detecting multimodal deception through visually grounded multi-agent debate, with MM-DeceptionBench.', 'quan2026blindspot': 'Evaluating biosecurity risks in language models with SPIKE-Bench and the Functional Harmfulness Rate.', 'chen2025deception': 'A systematic survey of AI deception: its definitions, mechanisms, risks, and mitigation strategies.', 'wang2026moralautonomy': 'A position paper on moral autonomy as an alignment goal, grounded in reflective endorsement, articulated principles, and practical wisdom.', 'ji2025selfmonitoring': 'Embedding a self-monitor in chain-of-thought reasoning to detect and suppress deceptive alignment.'}

# Match the original Jekyll bibliography's export behavior: website-only fields
# and display superscripts must not become part of a reader's citation.
bibtex_config = yaml.safe_load((SRC / "_config.yml").read_text()).get("filtered_bibtex_keywords")
if not isinstance(bibtex_config, list) or not all(isinstance(field, str) for field in bibtex_config):
    raise ValueError("filtered_bibtex_keywords must be a list of strings in _config.yml")
filtered_bibtex_fields = set(bibtex_config) | {"key", "raw"}

def citation(p, paper_url):
    kind = re.match(r"@(\w+)", p["raw"])[1]
    fields = {k: v for k, v in p.items() if k not in filtered_bibtex_fields}
    fields["author"] = re.sub(r"[*†‡§¶‖^]", "", fields["author"])
    fields.setdefault("url", paper_url)
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items())
    return f"@{kind}{{{p['key']},\n{body}\n}}"

def paper(p, prefix, zh):
    names = []
    for n in p['author'].split(' and '):
        (last, first) = n.split(', ', 1)
        name = esc((first + ' ' + last).replace('{\\`e}', 'è'))
        if 'Sitong Fang' in name:
            name = '<strong>' + name + '</strong>'
        elif 'Boyuan Chen' in name:
            name = '<a href="https://cby-pku.github.io/">' + name + '</a>'
        names.append('<span class="author">' + name + '</span>')
    authors = ', '.join(names)
    if len(names) > 12:
        authors = ', '.join(names[:3]) + ', et al.' + f"""<details class="authors-full"><summary>{('全部作者' if zh else 'All authors')}</summary><p>{authors}</p></details>"""
    paper_url = 'https://arxiv.org/abs/' + p['arxiv'] if 'arxiv' in p else p['html']
    links = [f'<a href="{paper_url}">paper</a>']
    for (k, label) in [('website', 'project page'), ('code', 'code')]:
        if k in p:
            links.append(f'<a href="{p[k]}">{label}</a>')
    venue = p.get('abbr', '')
    venue_html = f'<div class="venue">{esc(venue)}</div>' if venue else ''
    highlight = ' highlighted' if p['key'] == 'fang2026truthful' else ''
    media = f'''<a class="paper-image" href="{p.get('website', paper_url)}"><img src="{prefix}assets/homepage/{p['preview']}" alt="{esc(p['title'])} — research overview" loading="lazy" width="180" height="125"></a>''' if 'preview' in p else ''
    image_class = '' if media else ' no-preview'
    return f'''<article class="paper{highlight}{image_class}">{media}<div><h3><a href="{paper_url}">{esc(p['title'])}</a></h3><div class="authors">{authors}</div>{venue_html}{('<span class="equal">* Equal contribution</span>' if 'annotation' in p else '')}<div class="paper-links">{' <span aria-hidden="true">/</span> '.join(links)} <span aria-hidden="true">/</span> <details class="bib"><summary>BibTeX</summary><pre>{esc(citation(p, paper_url))}</pre></details></div><p class="paper-desc">{esc(short.get(p['key'], p.get('abstract', '')))}</p></div></article>'''

def rows(lines):
    out = ''
    for line in lines:
        m = re.match('- _(.*?)_\\s*&nbsp;\\s*(.*)', line)
        if m:
            out += f'<li><time>{m[1]}</time><div>{md(m[2])}</div></li>'
    return out

def make(zh=False):
    prefix = '../' if zh else ''
    s = (SRC / ('_pages/about_zh.md' if zh else '_pages/about.md')).read_text()
    biography = s.split('\n---\n', 1)[1].split('\n## ', 1)[0].strip()
    intro = ''.join(('<p>' + paragraph + '</p>' for paragraph in biography.split('\n\n')))

    def section(title):
        return s.split('## ' + title + '\n', 1)[1].split('\n## ', 1)[0].strip()
    news = section('动态' if zh else 'News').splitlines()
    awards = section('代表荣誉' if zh else 'Selected Honors').splitlines()
    labels = ['动态', '逆矩阵', '论文', '荣誉', '经历'] if zh else ['News', 'Physis AI', 'Publications', 'Honors', 'Experience']
    nav = '<span aria-hidden="true">/</span>'.join((f'<a href="#{key}">{label}</a>' for (key, label) in zip(['news', 'physis', 'research', 'awards', 'experience'], labels)))
    company = section('逆矩阵' if zh else 'Physis AI')
    order = ['fang2026truthful', 'fang2026debate', 'chen2025deception']
    order = [k for k in order if any(p['key'] == k and p.get('selected') == 'true' for p in papers)]
    order += [p['key'] for p in papers if p.get('selected') == 'true' and p['key'] not in order]
    ps = {p['key']: p for p in papers}
    pubs = ''.join((paper(ps[k], prefix, zh) for k in order))
    extra = ''.join((paper(ps[k], prefix, zh) for k in [p['key'] for p in sorted(papers, key=lambda p: (p.get('year', ''), p['key']), reverse=True) if p.get('selected') == 'false']))
    experience = section('经历' if zh else 'Experience')
    title = '方思童 · Sitong Fang' if zh else 'Sitong Fang'
    doc = f'''<!doctype html><html lang="{('zh-CN' if zh else 'en')}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Sitong Fang — partner at Physis AI, working on foundation model training for physical intelligence. Research interests include trustworthy multimodal AI."><title>{title}</title><link rel="canonical" href="https://sitongfang.com/{('zh/' if zh else '')}"><link rel="alternate" hreflang="en" href="https://sitongfang.com/"><link rel="alternate" hreflang="zh-CN" href="https://sitongfang.com/zh/"><link rel="alternate" hreflang="x-default" href="https://sitongfang.com/"><meta property="og:title" content="{title}"><meta property="og:type" content="website"><meta property="og:url" content="https://sitongfang.com/{('zh/' if zh else '')}"><link rel="icon" href="{prefix}assets/homepage/favicon.png"><link rel="stylesheet" href="{prefix}assets/homepage/style.css?v={stylesheet_version}"><script defer src="{prefix}assets/homepage/app.js"></script></head>\n<body><a class="skip" href="#main">{('跳至正文' if zh else 'Skip to content')}</a><div class="page"><div class="utility" aria-label="{('页面导航' if zh else 'Main navigation')}"><a href="{('../index.html' if zh else 'zh/index.html')}" lang="{('en' if zh else 'zh-CN')}">{('EN' if zh else '中文')}</a><button id="theme" type="button" aria-label="{('切换深色模式' if zh else 'Toggle dark mode')}" aria-pressed="false">◐</button></div>\n<main id="main"><header class="hero" id="about"><div class="intro"><h1>{title}</h1>{md(intro)}<div class="contacts"><a href="mailto:sitongfang1@gmail.com">Email</a><span aria-hidden="true">/</span><a href="https://scholar.google.com/citations?user=86JM-y0AAAAJ">Scholar</a><span aria-hidden="true">/</span><a href="https://github.com/Lavezlyn">GitHub</a><span aria-hidden="true">/</span><a href="{prefix}assets/pdf/CV_Sitong_Fang{('_zh' if zh else '')}.pdf">CV</a></div></div></header><nav aria-label="Section navigation">{nav}</nav>\n<section id="news"><div class="section-title"><h2>{labels[0]}</h2></div><ul class="dated news">{rows(news[:5])}</ul><details class="archive"><summary>{('更早动态' if zh else 'Earlier updates')}</summary><ul class="dated">{rows(news[5:])}</ul></details></section>\n<section id="physis"><div class="section-title"><h2>{('逆矩阵' if zh else 'Physis AI')}</h2><a class="section-note" href="https://physis-ai.com/">physis-ai.com ↗</a></div>{company}</section>\n<section id="research"><div class="section-title"><h2>{('代表论文' if zh else 'Selected Publications')}</h2><a class="section-note" href="https://scholar.google.com/citations?user=86JM-y0AAAAJ">Google Scholar ↗</a></div>{pubs}<details class="more-papers"><summary>{('更多论文' if zh else 'More publications')}</summary>{extra}</details></section>\n<section id="awards"><h2>{('代表荣誉' if zh else 'Selected Honors')}</h2><ul class="dated awards">{rows(awards)}</ul></section>\n<section id="experience"><h2>{('经历' if zh else 'Experience')}</h2>{experience}</section>\n</main><footer><span>© 2026 Sitong Fang · {('更新于' if zh else 'Updated')} Nov 2026</span><a href="#about">{('返回顶部' if zh else 'Back to top')} ↑</a></footer></div></body></html>'''
    dest = OUT / 'zh/index.html' if zh else OUT / 'index.html'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(doc)
make()
make(True)
print('Built English and Chinese homepages')
