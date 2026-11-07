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

{% assign presentations = site.posts | where_exp: "talk", "talk.presentation_status" | sort: "date" | reverse %}
{% if presentations.size > 0 %}

<span id="accepted-for-presentation"></span>

## Conference presentations

<ul>
{% for talk in presentations %}
  <li>
    <a href="{{ talk.url | relative_url }}">{{ talk.paper_title | escape }}</a><br>
    <strong>{{ talk.presentation_status | escape }}</strong> · {{ talk.presentation_event | escape }}
  </li>
{% endfor %}
</ul>
{% endif %}
