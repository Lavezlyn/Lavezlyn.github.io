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

[Project Page](https://truthfulvqa.github.io/){: .btn .btn-primary}
[Paper](https://arxiv.org/abs/2505.20214){: .btn .btn-secondary}
[Code](https://github.com/PKU-Alignment/TruthfulVQA){: .btn .btn-secondary}

---

### TL;DR

We discover that "slower" reasoning models (System II thinking) are **less truthful** than faster models in multimodal settings, and propose TruthfulVQA -- the first benchmark for evaluating multimodal truthfulness.

### Key Findings

1. **Inverse Scaling Law**: Slower, deeper reasoning models fabricate plausible but false details when given incomplete or misleading visual information, while faster chat models are more cautious.

2. **TruthfulVQA Benchmark**: The first open-source multimodal truthfulness benchmark with 5,000+ images across 8 categories and 21 subcategories, featuring a 3-level hierarchical prompt design.

3. **TruthfulJudge**: A reliable, human-in-the-loop evaluation framework that addresses the paradox of using potentially untruthful LLMs as truthfulness judges.

### BibTeX

```bibtex
@inproceedings{fang2026truthful,
  title={When Slower Isn't Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning},
  author={Fang, Sitong and Cao, Wenjing and Li, Jiahao and Wang, Xuyao and Chan, Chi-Min and Han, Sirui and Dai, Juntao and Guo, Yike and Yang, Yaodong and Ji, Jiaming},
  booktitle={ACL},
  year={2026}
}
```
