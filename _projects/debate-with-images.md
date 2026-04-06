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

### BibTeX

```bibtex
@inproceedings{fang2026debate,
  title={Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models},
  author={Fang, Sitong and Hou, Shiyi and Wang, Kaile and Chen, Boyuan and Hong, Donghai and Zhou, Jiayi and Dai, Juntao and Yang, Yaodong and Ji, Jiaming},
  booktitle={Under Review at ICML},
  year={2026}
}
```
