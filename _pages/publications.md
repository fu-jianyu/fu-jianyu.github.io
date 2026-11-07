---
layout: page
title: Publications
permalink: /publications/
nav: true
nav_order: 2
description: Journal articles and conference contributions by Jianyu Fu on urban perception, human mobility, and urban analytics.
---

See also my [Google Scholar](https://scholar.google.com/citations?user=zqWZAygAAAAJ) and [ORCID](https://orcid.org/0009-0006-1279-9675) profiles.

{% include bib_search.liquid %}

<div class="publications">
{% bibliography %}
</div>

{% assign presentations = site.posts | where: "presentation_status", "accepted" %}
{% if presentations.size > 0 %}

## Accepted for presentation

{% for talk in presentations %}

- [{{ talk.paper_title }}]({{ talk.url | relative_url }}) — {{ talk.description }} ({{ talk.date | date: "%-d %B %Y" }})
  {% endfor %}
  {% endif %}
