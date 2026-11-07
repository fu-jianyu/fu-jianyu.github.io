---
layout: post
title: Mapping streetscape emotions in Landscape and Urban Planning (IF 11.5)
date: 2026-11-03 12:00:00 +0900
description: R-ECoT uses public responses to cityscape photographs to estimate eight emotions and map them along streets in Setagaya, Tokyo.
thumbnail: /assets/img/research-updates/recot-workflow.jpg
og_image: https://fu-jianyu.github.io/assets/img/research-updates/recot-workflow.jpg
related_posts: false
---

Our paper, **“Evaluating urban street views through collective emotional perception from multimodal social media cityscape posts: An R-ECoT-based interpretable framework,”** was published online on **3 November 2026** in _Landscape and Urban Planning_ (Elsevier; **JCR Q1 · Impact Factor 11.5**). **DOI: [10.1016/j.landurbplan.2026.105822](https://doi.org/10.1016/j.landurbplan.2026.105822).**

I led this study as a doctoral researcher in the Sekimoto Lab at The University of Tokyo, with Xukang Wang, Jue Ma, Chenbo Zhao, Yoshiki Ogawa, and Yoshihide Sekimoto.

### Learning from comments on city photographs

What can the comments beneath a street photograph tell us about how people see that place? Through approved access to the Meta Content Library API in the SOMAR Virtual Data Enclave, we analyzed **1,078 Facebook and Instagram cityscape posts and 20,546 comments**. We used the comments to estimate the strength of Plutchik’s eight emotions for each photograph. A single scene could evoke several emotions at once, something a single positive or negative label would miss.

We used these estimates to train R-ECoT, a vision–language model that predicts an emotion profile from an image alone. For each prediction, it also highlights the parts of the photograph that contributed most. This makes it possible to inspect, for example, which parts of the same scene the model associates with joy and which it associates with fear.

{% include figure.liquid path="assets/img/research-updates/recot-workflow.jpg" alt="Workflow from social media comments and emotion labels through R-ECoT training to street-level mapping in Setagaya" class="img-fluid rounded" zoomable=true caption="How we learn from image–comment pairs and transfer the model to street-view photographs. Click to enlarge." %}

### From photographs to a street map

Across the models we tested, the CLIP-based version of R-ECoT performed best: **KL divergence 0.329, mean squared error 0.0106, and balanced accuracy 0.757**. We then applied it to **610,017 ZENRIN street-view images** in Setagaya Ward, Tokyo, and aggregated predictions along 10-metre road segments.

{% include figure.liquid path="assets/img/research-updates/recot-setagaya.jpg" alt="Eight maps of Setagaya showing predicted joy, sadness, trust, disgust, anticipation, surprise, anger, and fear, with street-view examples" class="img-fluid rounded" zoomable=true caption="Predicted emotion profiles across Setagaya’s street network. Each panel maps one emotion and shows example street views. Click to enlarge." %}

These maps show how the model interprets visible street conditions. They do not measure the feelings of individual pedestrians. For a planner, their value is in finding a segment worth visiting and then tracing its score back to the photograph: which features drew the model’s attention, and do they merit a closer look on site?
