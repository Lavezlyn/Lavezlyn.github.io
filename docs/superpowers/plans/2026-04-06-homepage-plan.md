# Sitong Fang Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a professional academic homepage for Sitong Fang using al-folio on GitHub Pages, with bilingual support and project pages.

**Architecture:** Fork al-folio Jekyll template into the existing `Lavezlyn.github.io` repo. All content goes in the about.md body for full layout control (matching cby-pku.github.io style). BibTeX-powered publications page auto-generates from papers.bib. Separate project pages per first-author paper. Simple Chinese about page with navbar link.

**Tech Stack:** Jekyll (al-folio template), GitHub Pages, GitHub Actions, jekyll-scholar (BibTeX), SCSS

**Spec:** `docs/superpowers/specs/2026-04-06-homepage-design.md`

---

### Task 1: Clone al-folio and configure base project

**Files:**
- Create: `_config.yml` (overwrite al-folio default)
- Create: `_data/socials.yml` (overwrite al-folio default)
- Create: `assets/img/prof_pic.jpg` (copy from `cv_photo.png`)
- Delete: al-folio example content (`_posts/`, `_news/`, `_projects/`, `_bibliography/papers.bib` defaults)

- [ ] **Step 1: Clone al-folio template into working directory**

```bash
cd /mnt/users/sitong/homepage
git clone --depth 1 https://github.com/alshedivat/al-folio.git /tmp/al-folio-template
# Copy al-folio files into working directory, preserving our docs/ and existing files
rsync -av --exclude='.git' /tmp/al-folio-template/ /mnt/users/sitong/homepage/
rm -rf /tmp/al-folio-template
```

- [ ] **Step 2: Remove al-folio example content**

```bash
cd /mnt/users/sitong/homepage
# Remove example blog posts
rm -f _posts/*
# Remove example news
rm -f _news/*
# Remove example projects
rm -f _projects/*
# Remove example bibliography
rm -f _bibliography/papers.bib
# Remove example assets
rm -f assets/img/prof_pic.jpg
rm -f assets/pdf/example_pdf.pdf
rm -f assets/json/resume.json
# Remove example pages we don't need
rm -f _pages/profiles.md _pages/repositories.md _pages/teaching.md _pages/books.md _pages/blog.md _pages/dropdown.md _pages/about_einstein.md
```

- [ ] **Step 3: Copy profile photo**

```bash
cp /mnt/users/sitong/homepage/cv_photo.png /mnt/users/sitong/homepage/assets/img/prof_pic.jpg
```

- [ ] **Step 4: Configure `_config.yml`**

Write the full `_config.yml` with these key settings:

```yaml
# --- Site Settings ---
title: ""
first_name: Sitong
middle_name:
last_name: Fang
email: sitongfang@stu.pku.edu.cn
description: "Sitong Fang's academic homepage. AI Safety & Alignment researcher at Peking University."
footer_text: ""
url: https://lavezlyn.github.io
baseurl: ""
last_updated: true

# --- Layout ---
navbar_fixed: true
footer_fixed: false
back_to_top: true
max_width: 930px

# --- Search ---
search_enabled: true
bib_search: true

# --- Dark Mode ---
enable_darkmode: true

# --- Collections ---
collections:
  news:
    defaults:
      layout: post
    output: true
    permalink: /news/:path/
  projects:
    output: true
    permalink: /projects/:path/

# --- Jekyll Scholar (Publications) ---
scholar:
  last_name: [Fang]
  first_name: [Sitong, S.]
  style: apa
  locale: en
  source: /_bibliography/
  bibliography: papers.bib
  bibliography_template: bib
  bibtex_filters: [latex, smallcaps, superscript]
  replace_strings: true
  join_strings: true
  details_dir: bibliography
  details_link: Details
  query: "@*"
  group_by: year
  group_order: descending

# --- Publication Badges ---
enable_publication_badges:
  altmetric: false
  dimensions: false
  google_scholar: true
  inspirehep: false

enable_publication_thumbnails: true

# --- Feature Toggles ---
enable_google_analytics: false
enable_masonry: true
enable_math: false
enable_tooltips: false
enable_navbar_social: false
enable_project_categories: false
enable_medium_zoom: true
enable_progressbar: true

# --- Social/Open Graph ---
serve_og_meta: true
og_image: /assets/img/prof_pic.jpg

# --- Plugins ---
plugins:
  - jekyll-paginate-v2
  - jekyll-archives-v2
  - jekyll-email-protect
  - jekyll-feed
  - jekyll-get-json
  - jekyll-imagemagick
  - jekyll-jupyter-notebook
  - jekyll-link-attributes
  - jekyll-minifier
  - jekyll-regex-replace
  - jekyll-scholar
  - jekyll-sitemap
  - jekyll-socials
  - jekyll-tabs
  - jekyll-toc
  - jekyll-twitter-plugin
  - jemoji

# --- Sass ---
sass:
  sass_dir: _sass
  style: compressed

# --- Outputting ---
permalink: /:categories/:title/
timezone: Asia/Shanghai

# --- Other ---
filtered_bibtex_keywords:
  [abbr, abstract, additional_info, altmetric, annotation, arxiv, award,
   award_name, bibtex_show, blog, code, dimensions, eprint,
   google_scholar_id, hal, html, inspirehep_id, pdf, pmid, poster,
   preview, selected, slides, supp, video, website]
```

- [ ] **Step 5: Configure `_data/socials.yml`**

```yaml
email: sitongfang@stu.pku.edu.cn
scholar_userid: 86JM-y0AAAAJ
github_username: Lavezlyn
# linkedin_username:  # add later if desired
# x_username:         # add later if desired
rss_icon: false
```

- [ ] **Step 6: Verify build works**

```bash
cd /mnt/users/sitong/homepage
bundle install
bundle exec jekyll build 2>&1 | tail -20
echo "Exit code: $?"
```

Expected: Build succeeds (exit code 0).

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat: initialize al-folio template with base configuration"
```

---

### Task 2: Write the About page (English)

**Files:**
- Create: `_pages/about.md` (overwrite al-folio default)

The about page contains ALL main content sections in the body, with auto-rendered selected_papers and announcements disabled (we control the order manually).

- [ ] **Step 1: Write `_pages/about.md`**

```markdown
---
layout: about
title: about
permalink: /
subtitle: >
  Undergraduate Student, <a href="https://yuanpei.pku.edu.cn/">Yuanpei College</a>, <a href="https://www.pku.edu.cn/">Peking University</a>

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true
  more_info: >
    <p>Beijing, China</p>
    <p>AI Safety & Alignment</p>

selected_papers: false
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false
---

I am an undergraduate student at [Peking University](https://www.pku.edu.cn/), majoring in Artificial Intelligence in the [Yuanpei Honors College](https://yuanpei.pku.edu.cn/). I am a member of the [PKU Alignment Group](https://github.com/PKU-Alignment), advised by [Prof. Yaodong Yang](https://www.yangyaodong.com/).

My research focuses on the **trustworthiness of multimodal AI systems**, with an emphasis on truthfulness evaluation, deception detection, and alignment. I have proposed [TruthfulVQA](https://arxiv.org/abs/2505.20214), the first benchmark for multimodal truthfulness, and [MM-DeceptionBench](https://arxiv.org/abs/2512.00349), the first benchmark for detecting deceptive behaviors in multimodal LLMs.

I have published at top AI venues including **ACL** and **ICML** (under review), with two first-author papers as an undergraduate.

## News

- *2026.01*: One paper accepted at **ACL 2026** Main Conference.
- *2025.12*: One paper submitted to **ICML 2026**.
- *2025.11*: Our survey [AI Deception](https://arxiv.org/abs/2511.22619) released -- the first systematic international report on AI deception (59 co-authors).
- *2025.10*: [Eval-Anything](https://github.com/PKU-Alignment/eval-anything) open-sourced at PKU-Alignment.
- *2024.12*: Awarded Beijing Natural Science Foundation Undergraduate "QiYan" Research Program Grant.

## Honors and Awards

- *2025* &nbsp; Yuanpei Young Scholar (元培青年学者, Top 10 across all grades)
- *2025* &nbsp; Soong Ching Ling Future Scholarship (宋庆龄未来助学金)
- *2025* &nbsp; Beijing Natural Science Foundation Undergraduate "QiYan" Research Program (北京市自然科学基金本科生"启研"计划)
- *2024* &nbsp; Peking University Boya Scholarship
- *2024* &nbsp; Peking University CMSC Scholarship (招商证券奖学金)
- *2024* &nbsp; Academic Excellence Award
- *2024* &nbsp; Social Service Award
- *2023* &nbsp; Peking University Freshman Scholarship (First Prize)
- *2023* &nbsp; Provincial Top 1, National College Entrance Exam (Science)

## Selected Publications

<div class="publications">
{% bibliography --query @*[selected=true] %}
</div>

## Experiences

<div class="experience-item" style="margin-bottom: 1rem;">
<strong>HKGAI R&D Center / HKUST</strong><br>
Contributed to <strong>HKGAI-V1</strong>, the Hong Kong government's first locally fine-tuned generative AI model based on DeepSeek. Supports Cantonese, Mandarin, and English with localized safety alignment. Received recognition certificate from HKUST and HKGAI R&D Center.
</div>

<div class="experience-item" style="margin-bottom: 1rem;">
<strong>PKU-Alignment, Peking University</strong> — Core Contributor<br>
<ul>
<li><a href="https://github.com/PKU-Alignment/align-anything">Align-Anything</a> (4.6k+ ★) — All-modality alignment framework</li>
<li><a href="https://github.com/PKU-Alignment/eval-anything">Eval-Anything</a> — All-modality safety evaluation framework</li>
</ul>
</div>

## Educations

- *2023 - Present* &nbsp; B.S. in Artificial Intelligence, Yuanpei Honors College, Peking University
```

**Note:** The exact years for awards are estimates from the spec. Confirm with user during review. The news dates (month) should also be confirmed. The email in _config.yml should be verified.

- [ ] **Step 2: Verify build**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1 | tail -20
```

Expected: Build succeeds. The `{% bibliography %}` tag may warn if papers.bib doesn't exist yet -- that's OK, we'll add it in Task 3.

- [ ] **Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "feat: add About page with bio, news, awards, experiences, education"
```

---

### Task 3: Set up BibTeX publications system

**Files:**
- Create: `_bibliography/papers.bib`
- Create: `_data/venues.yml`
- Modify: `_pages/publications.md` (confirm configuration)
- Create: `assets/img/publication_preview/` directory (placeholder images for now)

- [ ] **Step 1: Write `_bibliography/papers.bib`**

```bibtex
@inproceedings{fang2026truthful,
  title     = {When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning},
  author    = {Fang, Sitong and Cao, Wenjing and Li, Jiahao and Wang, Xuyao and Chan, Chi-Min and Han, Sirui and Dai, Juntao and Guo, Yike and Yang, Yaodong and Ji, Jiaming},
  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2026},
  abbr      = {ACL},
  abstract  = {We investigate truthfulness in multimodal large language models and discover an inverse scaling law: slower reasoning models are less truthful in multimodal settings. We propose TruthfulVQA, the first benchmark for multimodal truthfulness evaluation, and TruthfulJudge, a reliable human-in-the-loop evaluation framework.},
  arxiv     = {2505.20214},
  code      = {https://github.com/PKU-Alignment/TruthfulVQA},
  selected  = {true},
  preview   = {truthfulvqa.png},
  bibtex_show = {true},
  website   = {/projects/truthfulvqa/}
}

@inproceedings{fang2026debate,
  title     = {Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models},
  author    = {Fang, Sitong and Hou, Shiyi and Wang, Kaile and Chen, Boyuan and Hong, Donghai and Zhou, Jiayi and Dai, Juntao and Yang, Yaodong and Ji, Jiaming},
  booktitle = {Under Review at the International Conference on Machine Learning (ICML)},
  year      = {2026},
  abbr      = {ICML},
  abstract  = {We introduce MM-DeceptionBench, the first benchmark for evaluating deceptive behaviors in multimodal LLMs, and propose Debate with Images, a multi-agent debate framework requiring models to ground claims in visual evidence. Our approach significantly improves deception detection accuracy and human agreement.},
  arxiv     = {2512.00349},
  code      = {https://github.com/PKU-Alignment/MM-DeceptionBench},
  selected  = {true},
  preview   = {debate_with_images.png},
  bibtex_show = {true},
  website   = {/projects/debate-with-images/}
}

@article{chen2025deception,
  title     = {AI Deception: Risks, Dynamics, and Controls},
  author    = {Chen*, Boyuan and Fang*, Sitong and Ji*, Jiaming and Zhu*, Yanxu and Wen*, Pengcheng and Wu*, Jinzhou and Tan, Yingshui and Zheng, Boren and Yuan, Mengying and Chen, Wenqi and Hong, Donghai and Qiu, Alex and Chen, Xin and Zhou, Jiayi and Wang, Kaile and Dai, Juntao and Zhang, Borong and Yang, Tianzhuo and Siddiqui, Saad and Duan, Isabella and Duan, Yawen and Tse, Brian and Huang, Jen-Tse and Wang, Kun and Zheng, Baihui and Liu, Jiaheng and Yang, Jian and Li, Yiming and Chen, Wenting and Liu, Dongrui and Vierling, Lukas and Xi, Zhiheng and Fu, Haobo and Wang, Wenxuan and Sang, Jitao and Shi, Zhengyan and Chan, Chi-Min and Shi, Eugenie and Li, Simin and Li, Juncheng and Yang, Jian and Ji, Wei and Li, Dong and Yang, Jinglin and Song, Jun and Dong, Yinpeng and Fu, Jie and Zheng, Bo and Yang, Min and Guo, Yike and Torr, Philip and Trager, Robert and Zeng, Yi and Wang, Zhongyuan and Yang, Yaodong and Huang, Tiejun and Zhang, Ya-Qin and Zhang, HongJiang and Yao, Andrew},
  journal   = {arXiv preprint},
  year      = {2025},
  abbr      = {Preprint},
  abstract  = {The first systematic international report on AI deception. We formally define AI deception using signaling theory, analyze the deception cycle, and propose mitigation strategies. A living database is maintained at deceptionsurvey.com.},
  arxiv     = {2511.22619},
  website   = {https://deceptionsurvey.com},
  bibtex_show = {true},
  preview   = {ai_deception.png}
}

@article{ji2025selfmonitoring,
  title     = {Mitigating Deceptive Alignment via Self-Monitoring},
  author    = {Ji*, Jiaming and Chen*, Wenqi and Wang*, Kaile and Hong, Donghai and Fang, Sitong and Chen, Boyuan and Zhou, Jiayi and Dai, Juntao and Han, Sirui and Guo, Yike and Yang, Yaodong},
  journal   = {arXiv preprint},
  year      = {2025},
  abbr      = {Preprint},
  abstract  = {We propose CoT Monitor+, a framework that embeds a Self-Monitor inside chain-of-thought reasoning to detect and suppress deceptive alignment. We also introduce DeceptionBench, a five-category benchmark. Our approach reduces deceptive behaviors by 43.8\% while preserving task accuracy.},
  arxiv     = {2505.18807},
  code      = {https://cot-monitor-plus.github.io/},
  bibtex_show = {true},
  preview   = {self_monitoring.png}
}
```

- [ ] **Step 2: Write `_data/venues.yml`**

```yaml
ACL:
  url: https://aclanthology.org/
  color: "#1a5276"

ICML:
  url: https://icml.cc/
  color: "#7d3c98"

NeurIPS:
  url: https://neurips.cc/
  color: "#c0392b"

ICLR:
  url: https://iclr.cc/
  color: "#27ae60"

Preprint:
  color: "#7f8c8d"
```

- [ ] **Step 3: Create placeholder publication preview images**

```bash
mkdir -p /mnt/users/sitong/homepage/assets/img/publication_preview
# Create simple placeholder images (these should be replaced with actual teaser figures)
# For now, create 200x200 colored placeholders
convert -size 400x300 xc:"#1a5276" -gravity center -pointsize 24 -fill white -annotate 0 "TruthfulVQA" assets/img/publication_preview/truthfulvqa.png 2>/dev/null || touch assets/img/publication_preview/truthfulvqa.png
convert -size 400x300 xc:"#7d3c98" -gravity center -pointsize 24 -fill white -annotate 0 "Debate" assets/img/publication_preview/debate_with_images.png 2>/dev/null || touch assets/img/publication_preview/debate_with_images.png
convert -size 400x300 xc:"#c0392b" -gravity center -pointsize 24 -fill white -annotate 0 "AI Deception" assets/img/publication_preview/ai_deception.png 2>/dev/null || touch assets/img/publication_preview/ai_deception.png
convert -size 400x300 xc:"#27ae60" -gravity center -pointsize 24 -fill white -annotate 0 "CoT Monitor+" assets/img/publication_preview/self_monitoring.png 2>/dev/null || touch assets/img/publication_preview/self_monitoring.png
```

**Note:** Replace these placeholders with actual paper teaser figures (from arxiv papers or presentation slides) during review.

- [ ] **Step 4: Configure `_pages/publications.md`**

```yaml
---
layout: page
permalink: /publications/
title: Publications
description: Publications in reverse chronological order.
nav: true
nav_order: 2
---

{% include bib_search.liquid %}

<div class="publications">
{% bibliography %}
</div>
```

- [ ] **Step 5: Verify build and check publications render**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1 | tail -20
# Check that publications page was generated
ls _site/publications/index.html
```

Expected: Build succeeds. `_site/publications/index.html` exists.

- [ ] **Step 6: Commit**

```bash
git add _bibliography/papers.bib _data/venues.yml _pages/publications.md assets/img/publication_preview/
git commit -m "feat: add BibTeX publications with 4 papers and venue badges"
```

---

### Task 4: Create project pages for first-author papers

**Files:**
- Modify: `_pages/projects.md`
- Create: `_projects/truthfulvqa.md`
- Create: `_projects/debate-with-images.md`

- [ ] **Step 1: Configure `_pages/projects.md`**

```yaml
---
layout: page
title: Projects
permalink: /projects/
description: Research projects with demos, code, and datasets.
nav: true
nav_order: 3
display_categories: []
horizontal: false
---
```

- [ ] **Step 2: Create `_projects/truthfulvqa.md`**

```markdown
---
layout: page
title: "When Slower Isn't Truer"
description: "Inverse Scaling Law of Truthfulness in Multimodal Reasoning"
img: assets/img/publication_preview/truthfulvqa.png
importance: 1
category: research
---

## When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning

**Sitong Fang**, Wenjing Cao, Jiahao Li, Xuyao Wang, Chi-Min Chan, Sirui Han, Juntao Dai, Yike Guo, Yaodong Yang, Jiaming Ji

**ACL 2026 Main Conference**

[Paper](https://arxiv.org/abs/2505.20214){: .btn .btn-primary}
[Code](https://github.com/PKU-Alignment/TruthfulVQA){: .btn .btn-secondary}

---

### TL;DR

We discover that "slower" reasoning models (System II thinking) are **less truthful** than faster models in multimodal settings, and propose TruthfulVQA -- the first benchmark for evaluating multimodal truthfulness.

### Key Findings

1. **Inverse Scaling Law**: Slower, deeper reasoning models fabricate plausible but false details when given incomplete or misleading visual information, while faster chat models are more cautious.

2. **TruthfulVQA Benchmark**: The first open-source multimodal truthfulness benchmark with 5,000+ images across 8 categories and 21 subcategories, featuring a 3-level hierarchical prompt design.

3. **TruthfulJudge**: A reliable, human-in-the-loop evaluation framework that addresses the paradox of using potentially untruthful LLMs as truthfulness judges.

### Abstract

{% raw %}{% bibliography --query @*[key=fang2026truthful] %}{% endraw %}

### BibTeX

```bibtex
@inproceedings{fang2026truthful,
  title={When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning},
  author={Fang, Sitong and Cao, Wenjing and Li, Jiahao and Wang, Xuyao and Chan, Chi-Min and Han, Sirui and Dai, Juntao and Guo, Yike and Yang, Yaodong and Ji, Jiaming},
  booktitle={ACL},
  year={2026}
}
```
---

- [ ] **Step 3: Create `_projects/debate-with-images.md`**

```markdown
---
layout: page
title: "Debate with Images"
description: "Detecting Deceptive Behaviors in Multimodal Large Language Models"
img: assets/img/publication_preview/debate_with_images.png
importance: 2
category: research
---

## Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models

**Sitong Fang**, Shiyi Hou, Kaile Wang, Boyuan Chen, Donghai Hong, Jiayi Zhou, Juntao Dai, Yaodong Yang, Jiaming Ji

**Under Review at ICML 2026**

[Paper](https://arxiv.org/abs/2512.00349){: .btn .btn-primary}
[Code](https://github.com/PKU-Alignment/MM-DeceptionBench){: .btn .btn-secondary}

---

### TL;DR

We introduce **MM-DeceptionBench**, the first benchmark for evaluating deceptive behaviors in multimodal LLMs, and propose a multi-agent **Debate with Images** framework that grounds claims in visual evidence to detect AI deception.

### Key Findings

1. **MM-DeceptionBench**: 1,013 cases with 1,096 images (95%+ real-world), covering 6 deception types: Sycophancy, Sandbagging, Bluffing, Obfuscation, Deliberate Omission, and Fabrication.

2. **Debate with Images Framework**: A multi-agent debate mechanism requiring models to ground every claim in visual evidence, significantly improving deception detection.

3. **Results**: Detection accuracy improved from 61.5% to 76.0%, with Cohen's Kappa (human agreement) increasing by nearly 1.5x. Generalizable to safety (PKU-SafeRLHF-V) and reasoning (HallusionBench) tasks.

### Abstract

{% raw %}{% bibliography --query @*[key=fang2026debate] %}{% endraw %}

### BibTeX

```bibtex
@inproceedings{fang2026debate,
  title={Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models},
  author={Fang, Sitong and Hou, Shiyi and Wang, Kaile and Chen, Boyuan and Hong, Donghai and Zhou, Jiayi and Dai, Juntao and Yang, Yaodong and Ji, Jiaming},
  booktitle={Under Review at ICML},
  year={2026}
}
```
```

- [ ] **Step 4: Verify build**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1 | tail -20
ls _site/projects/
```

Expected: Build succeeds. Project pages generated.

- [ ] **Step 5: Commit**

```bash
git add _pages/projects.md _projects/
git commit -m "feat: add project pages for TruthfulVQA and Debate with Images"
```

---

### Task 5: Set up CV page

**Files:**
- Modify: `_pages/cv.md`
- Create: `assets/pdf/CV_Sitong_Fang.pdf` (placeholder — user provides actual PDF)

- [ ] **Step 1: Write `_pages/cv.md`**

```yaml
---
layout: cv
permalink: /cv/
title: CV
nav: true
nav_order: 4
cv_pdf: /assets/pdf/CV_Sitong_Fang.pdf
description: ""
---
```

- [ ] **Step 2: Create placeholder CV PDF**

```bash
mkdir -p /mnt/users/sitong/homepage/assets/pdf
# Create a minimal placeholder PDF
echo "%PDF-1.0
1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj
2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj
3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R>>endobj
xref
0 4
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
trailer<</Size 4/Root 1 0 R>>
startxref
190
%%EOF" > /mnt/users/sitong/homepage/assets/pdf/CV_Sitong_Fang.pdf
```

**Note:** Replace this placeholder with the actual CV PDF. The user should export their CV as PDF and place it at `assets/pdf/CV_Sitong_Fang.pdf`.

- [ ] **Step 3: Verify build**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1 | tail -20
ls _site/cv/index.html
```

- [ ] **Step 4: Commit**

```bash
git add _pages/cv.md assets/pdf/CV_Sitong_Fang.pdf
git commit -m "feat: add CV page with PDF download"
```

---

### Task 6: Add Chinese About page

**Files:**
- Create: `_pages/about_zh.md`
- Modify: `_config.yml` (add Chinese page to navbar via `header_pages` or handle in the page itself)

Strategy: Simple separate page at `/zh/` with a navbar link. Not full i18n (can upgrade later).

- [ ] **Step 1: Write `_pages/about_zh.md`**

```markdown
---
layout: about
title: 中文
permalink: /zh/
subtitle: >
  本科生, <a href="https://yuanpei.pku.edu.cn/">元培学院</a>, <a href="https://www.pku.edu.cn/">北京大学</a>
nav: true
nav_order: 6

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true
  more_info: >
    <p>北京</p>
    <p>AI 安全与对齐</p>

selected_papers: false
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false
---

我是[北京大学](https://www.pku.edu.cn/)[元培学院](https://yuanpei.pku.edu.cn/)人工智能专业本科生，通用人工智能实验班成员。我是[北大对齐小组](https://github.com/PKU-Alignment)成员，导师为[杨耀东](https://www.yangyaodong.com/)助理教授。

我的研究聚焦于**多模态人工智能系统的可信性**，重点方向包括真实性评估、欺骗检测与对齐。我提出了 [TruthfulVQA](https://arxiv.org/abs/2505.20214)（首个多模态真实性基准）和 [MM-DeceptionBench](https://arxiv.org/abs/2512.00349)（首个多模态大模型欺骗检测基准）。

我在本科期间已发表两篇一作论文于顶级人工智能会议，包括 **ACL 2026** 和 **ICML 2026**（审稿中）。

## 动态

- *2026.01*: 一篇论文被 **ACL 2026** 主会录用。
- *2025.12*: 一篇论文投稿至 **ICML 2026**。
- *2025.11*: 国际 AI 欺骗系统性报告 [AI Deception](https://arxiv.org/abs/2511.22619) 发布，59 位共同作者。
- *2025.10*: [Eval-Anything](https://github.com/PKU-Alignment/eval-anything) 在 PKU-Alignment 开源。
- *2024.12*: 获北京市自然科学基金本科生"启研"计划资助。

## 荣誉与奖项

- *2025* &nbsp; 元培青年学者（全年级仅 10 人）
- *2025* &nbsp; 宋庆龄未来助学金
- *2025* &nbsp; 北京市自然科学基金本科生"启研"计划
- *2024* &nbsp; 北京大学博雅奖学金
- *2024* &nbsp; 北京大学招商证券奖学金
- *2024* &nbsp; 学习优秀奖
- *2024* &nbsp; 社会工作奖
- *2023* &nbsp; 北京大学新生奖学金（一等奖）
- *2023* &nbsp; 高考理科状元

## 代表论文

<div class="publications">
{% bibliography --query @*[selected=true] %}
</div>

## 经历

<div class="experience-item" style="margin-bottom: 1rem;">
<strong>香港生成式人工智能研发中心 / 香港科技大学</strong><br>
参与开发 <strong>HKGAI-V1</strong>，香港政府首个基于 DeepSeek 模型进行全参数微调的本地生成式 AI 模型。支援粤语、普通话及英语，具备安全性与语境适切性。获香港科技大学及 HKGAI 研发中心授予表彰证书。
</div>

<div class="experience-item" style="margin-bottom: 1rem;">
<strong>北大对齐小组，北京大学</strong> — 核心贡献者<br>
<ul>
<li><a href="https://github.com/PKU-Alignment/align-anything">Align-Anything</a> (4.6k+ ★) — 全模态对齐框架</li>
<li><a href="https://github.com/PKU-Alignment/eval-anything">Eval-Anything</a> — 全模态安全评测框架</li>
</ul>
</div>

## 教育经历

- *2023 - 至今* &nbsp; 北京大学元培学院，人工智能专业
```

- [ ] **Step 2: Verify build**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1 | tail -20
ls _site/zh/index.html
```

Expected: Build succeeds. Chinese page generated at `/zh/`.

- [ ] **Step 3: Commit**

```bash
git add _pages/about_zh.md
git commit -m "feat: add Chinese version of About page at /zh/"
```

---

### Task 7: Clean up, configure deployment, and final test

**Files:**
- Clean: Remove remaining al-folio example files
- Verify: `.github/workflows/deploy.yml` (should come with al-folio)
- Verify: Full site build

- [ ] **Step 1: Clean up remaining example files**

```bash
cd /mnt/users/sitong/homepage
# Remove example data files
rm -f _data/coauthors.yml _data/repositories.yml
# Remove example CV data (user will provide their own)
rm -f _data/cv.yml
# Remove unused pages
rm -f _pages/news.md 2>/dev/null
# Remove any remaining example images
rm -f assets/img/prof_pic.jpg.bak 2>/dev/null
```

- [ ] **Step 2: Create `_data/coauthors.yml` with key collaborators**

```yaml
"yang":
  - firstname: ["Yaodong"]
    url: https://www.yangyaodong.com/

"ji":
  - firstname: ["Jiaming"]
    url: https://jiamingji.github.io/

"chen":
  - firstname: ["Boyuan"]
    url: https://cby-pku.github.io/
```

- [ ] **Step 3: Verify GitHub Actions workflow exists**

```bash
ls /mnt/users/sitong/homepage/.github/workflows/deploy.yml
cat /mnt/users/sitong/homepage/.github/workflows/deploy.yml | head -30
```

Expected: File exists (comes with al-folio).

- [ ] **Step 4: Full build test**

```bash
cd /mnt/users/sitong/homepage
bundle exec jekyll build 2>&1
echo "Exit code: $?"
echo "---"
echo "Generated pages:"
find _site -name "index.html" | sort
```

Expected: Exit code 0. Pages generated for `/`, `/publications/`, `/projects/`, `/cv/`, `/zh/`.

- [ ] **Step 5: Verify key pages have content**

```bash
# Check about page has bio content
grep -l "Sitong Fang" _site/index.html
# Check publications page has papers
grep -l "TruthfulVQA" _site/publications/index.html
# Check Chinese page exists
grep -l "元培" _site/zh/index.html
# Check project pages
grep -l "Debate with Images" _site/projects/debate-with-images/index.html
```

Expected: All greps match.

- [ ] **Step 6: Final commit**

```bash
git add -A
git commit -m "feat: clean up examples and finalize site configuration"
```

- [ ] **Step 7: Summary of what to do before pushing to GitHub**

Before pushing to `Lavezlyn/Lavezlyn.github.io`:

1. **Replace placeholder images**: Add actual paper teaser figures to `assets/img/publication_preview/`
2. **Replace CV PDF**: Put real CV at `assets/pdf/CV_Sitong_Fang.pdf`
3. **Verify email**: Confirm `sitongfang@stu.pku.edu.cn` is correct in `_config.yml` and `_data/socials.yml`
4. **Verify award years**: Check all years in about.md and about_zh.md are accurate
5. **Verify news dates**: Confirm exact months for news items
6. **Verify paper details**: Check all author lists, arXiv IDs, and code links in `papers.bib`
7. **Set up GitHub repo**: In repo Settings > Actions > Workflow permissions, enable "Read and write permissions"
8. **Push and deploy**:
   ```bash
   git remote set-url origin git@github.com:Lavezlyn/Lavezlyn.github.io.git
   git push -f origin master:main
   ```
9. **Enable Pages**: In repo Settings > Pages, set source branch to `gh-pages`

---

## File Map Summary

```
/mnt/users/sitong/homepage/
├── _config.yml                              # Site configuration
├── _data/
│   ├── socials.yml                          # Social links + email
│   ├── venues.yml                           # Publication venue colors
│   └── coauthors.yml                        # Co-author links
├── _bibliography/
│   └── papers.bib                           # All publications (4 papers)
├── _pages/
│   ├── about.md                             # English homepage
│   ├── about_zh.md                          # Chinese homepage (/zh/)
│   ├── publications.md                      # Publications list page
│   ├── projects.md                          # Projects landing page
│   └── cv.md                                # CV page
├── _projects/
│   ├── truthfulvqa.md                       # ACL 2026 project page
│   └── debate-with-images.md                # ICML 2026 project page
├── assets/
│   ├── img/
│   │   ├── prof_pic.jpg                     # Profile photo
│   │   └── publication_preview/
│   │       ├── truthfulvqa.png              # Paper teaser (replace)
│   │       ├── debate_with_images.png       # Paper teaser (replace)
│   │       ├── ai_deception.png             # Paper teaser (replace)
│   │       └── self_monitoring.png          # Paper teaser (replace)
│   └── pdf/
│       └── CV_Sitong_Fang.pdf               # CV PDF (replace)
├── docs/
│   └── superpowers/
│       ├── specs/2026-04-06-homepage-design.md
│       └── plans/2026-04-06-homepage-plan.md
└── .github/
    └── workflows/
        └── deploy.yml                       # GitHub Pages deployment
```
