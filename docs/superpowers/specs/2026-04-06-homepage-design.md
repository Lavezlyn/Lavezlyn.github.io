# Sitong Fang Academic Homepage — Design Spec

**Date**: 2026-04-06
**Status**: Approved
**Framework**: al-folio (Jekyll) on GitHub Pages

---

## 1. Goals & Target Audience

### Primary Goals (ordered by priority)
1. **PhD/Postdoc Applications** — Enable prospective advisors to assess research capability within 30 seconds
2. **Academic Reputation** — Make publications and contributions easily discoverable by peers and collaborators
3. **Scholarship/Fellowship Applications** — Present a complete academic profile for reviewers

### Target Audiences
- Prospective PhD advisors (international)
- Research collaborators in AI Safety/Alignment
- Scholarship/fellowship review committees
- Conference organizers

---

## 2. Technical Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Framework | al-folio (Jekyll) | ML community standard, native BibTeX/i18n/project pages |
| Hosting | GitHub Pages | Free, reliable, custom domain support |
| Repository | Lavezlyn/Lavezlyn.github.io | Existing GitHub username |
| Languages | English (primary `/`), Chinese (`/zh/`) | International + domestic audiences |
| CI/CD | GitHub Actions | Auto-build Jekyll, Google Scholar stats crawler |

---

## 3. Information Architecture

### 3.1 Main Page (`about.md`)

Layout reference: [cby-pku.github.io](https://cby-pku.github.io/)

Sections in order:

#### Hero Section
- Professional photo (`cv_photo.png`)
- Name: Sitong Fang (方思童)
- Title: Undergraduate Student
- Affiliation: Yuanpei College, Peking University
- Social links: Email, Google Scholar, GitHub (add LinkedIn/Twitter later if desired)

#### Bio (Bilingual)

**English:**
> I am an undergraduate student at Peking University, majoring in Artificial Intelligence in the Yuanpei Honors College. I am a member of the PKU Alignment Group, advised by Prof. Yaodong Yang.
>
> My research focuses on the trustworthiness of multimodal AI systems, with an emphasis on truthfulness evaluation, deception detection, and alignment. I have proposed TruthfulVQA, the first benchmark for multimodal truthfulness, and MM-DeceptionBench, the first benchmark for detecting deceptive behaviors in multimodal LLMs.
>
> I have published at top AI venues including ACL and ICML (under review), with two first-author papers as an undergraduate.

**Chinese:** Parallel translation with additional context for domestic awards.

#### News (5-8 items)
```
- [2026.01] One paper accepted at ACL 2026 Main Conference!
- [2025.xx] One paper submitted to ICML 2026.
- [2025.xx] Our survey "AI Deception" released — the first systematic
            international report on AI deception (59 co-authors).
- [2025.xx] Eval-Anything open-sourced at PKU-Alignment.
- [2024.xx] Awarded Beijing Natural Science Foundation Undergraduate
            "QiYan" Research Program Grant.
```

#### Honors and Awards (ordered by prestige, gaokao last)
1. Yuanpei Young Scholar (元培青年学者, Top 10 across all grades)
2. Soong Ching Ling Future Scholarship (宋庆龄未来助学金)
3. Beijing Natural Science Foundation Undergraduate "QiYan" Research Program (北京市自然科学基金本科生"启研"计划)
4. Peking University Freshman Scholarship (First Prize)
5. Peking University Boya Scholarship
6. Peking University CMSC Scholarship
7. Academic Excellence Award
8. Social Service Award
9. Provincial Top 1, National College Entrance Exam (Science, 2023)

#### Selected Publications (2-3 representative papers)

Display format per paper:
- Conference badge (colored label: ACL blue, ICML purple)
- Teaser/thumbnail image
- Title
- Authors (self bolded, co-first with `*`)
- One-line contribution summary
- Links: [Paper] [Code] [Project Page] [BibTeX]
- First-author papers marked with ★

Papers to feature:
1. ★ **When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning** — ACL 2026 Main
2. ★ **Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models** — Under Review at ICML 2026

#### Experiences
1. **HKGAI R&D Center / HKUST** — Contributed to HKGAI-V1, the Hong Kong government's first locally fine-tuned generative AI model based on DeepSeek. Supports Cantonese, Mandarin, and English with localized safety alignment. Received recognition certificate from HKUST and HKGAI R&D Center.
2. **PKU-Alignment, Peking University** — Core contributor to open-source projects:
   - Align-Anything (4.6k+ ★) — All-modality alignment framework
   - Eval-Anything — All-modality safety evaluation framework

#### Educations
- B.S. in Artificial Intelligence, Yuanpei Honors College, Peking University, 2023 – Present

### 3.2 Publications Page (`/publications/`)

- Full list, reverse chronological by year
- Auto-generated from `_bibliography/papers.bib` (al-folio native)
- Self name bolded, co-first authors marked with `*`
- First-author papers marked with ★
- Conference name as colored badge
- Links: [Paper] [Code] [Project] [BibTeX] per entry

**Papers:**

[2026]
- ★ When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning. **Sitong Fang**, Wenjing Cao, Jiahao Li, Xuyao Wang, Chi-Min Chan, Sirui Han, Juntao Dai, Yike Guo, Yaodong Yang, Jiaming Ji. **ACL 2026 Main Conference**.
- ★ Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models. **Sitong Fang**, Shiyi Hou, Kaile Wang, Boyuan Chen, Donghai Hong, Jiayi Zhou, Juntao Dai, Yaodong Yang, Jiaming Ji. **Under Review at ICML 2026**.

[2025]
- AI Deception: Risks, Dynamics, and Controls. Boyuan Chen\*, **Sitong Fang**\*, Jiaming Ji\*, ... (59 authors). Preprint.
- Mitigating Deceptive Alignment via Self-Monitoring. Jiaming Ji\*, Wenqi Chen\*, Kaile Wang\*, Donghai Hong, **Sitong Fang**, Boyuan Chen, Jiayi Zhou, Juntao Dai, Sirui Han, Yike Guo, Yaodong Yang. Preprint.

### 3.3 Project Pages (`/projects/`)

One page per first-author paper:

**`/projects/truthfulvqa/`** (When Slower Isn't Truer)
- Teaser figure (large, visual impact)
- TL;DR (one sentence)
- Abstract
- Key Findings (2-3 core results with figures)
- Method Overview (framework diagram)
- BibTeX
- Links: [Paper PDF] [Code] [Dataset] [Slides]

**`/projects/debate-with-images/`** (Debate with Images)
- Same structure
- Highlight: MM-DeceptionBench benchmark + multi-agent debate framework

### 3.4 CV Page (`/cv/`)

- Rendered HTML version of CV
- PDF download button
- Content mirrors the homepage but in formal CV format

---

## 4. Bilingual Strategy

| Aspect | Approach |
|--------|----------|
| Primary language | English (`/`) |
| Chinese path | `/zh/` via al-folio `_i18n/` |
| Switch UI | Language toggle button in navbar (top-right) |
| Translated content | Bio, News, Awards, Experiences, Educations |
| English-only content | Publications (titles, abstracts), Project Pages |
| Chinese extras | Full Chinese names for domestic awards, 元培青年学者 context |

---

## 5. Visual Design

| Element | Specification |
|---------|---------------|
| Color scheme | al-folio default (clean, muted) with minor accent customization |
| Typography | al-folio default (professional serif/sans-serif) |
| Photo | `cv_photo.png` — professional headshot, navy blouse, neutral background |
| Conference badges | Colored labels: ACL (blue), ICML (purple), Preprint (gray) |
| Paper thumbnails | Teaser figures from each paper |
| Responsive | al-folio native responsive design |
| Dark mode | al-folio native dark mode toggle |

---

## 6. Deployment

- **Repository**: `Lavezlyn/Lavezlyn.github.io` (existing)
- **Branch**: `main` (source), GitHub Actions builds to `gh-pages`
- **Domain**: `lavezlyn.github.io` (default), optional custom domain later
- **Google Scholar crawler**: Reuse existing `google_scholar_crawler/` with GitHub Actions for auto-updating citation stats

---

## 7. Research Narrative (embedded in Bio)

Three intertwined research threads (expressed through Bio text + publication structure):

1. **Truthfulness in Multimodal AI** — TruthfulVQA benchmark reveals inverse scaling law: slower reasoning models are less truthful in multimodal settings (ACL 2026)
2. **Multimodal Deception Detection** — MM-DeceptionBench + Debate with Images framework for detecting strategic deceptive behaviors in MLLMs (ICML 2026 under review)
3. **Systematic Deception Governance** — First international AI deception report (59 co-authors) + CoT Monitor+ for deceptive alignment mitigation

Narrative arc: Discovering the problem → Building detection tools → Toward systematic governance

---

## 8. Content Not Included (YAGNI)

- No blog/technical writing section (can add later)
- No video introduction
- No teaching/mentoring section
- No interactive demos (can embed HuggingFace Spaces in project pages later)
- No separate Research Statement page (narrative in Bio)
