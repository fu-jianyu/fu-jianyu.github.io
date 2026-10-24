---
layout: page
permalink: /blog/
title: Updates
description: Publications, research visits, and academic news.
nav: true
nav_order: 4
_styles: |
  .update-list { display: grid; gap: 2.5rem; }
  .update-item { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 2fr); gap: 1.5rem; align-items: start; border-bottom: 1px solid var(--global-divider-color); padding-bottom: 2rem; }
  .update-item img { width: 100%; height: auto; border-radius: .4rem; }
  .update-item h2 { margin-top: 0; }
  @media (max-width: 600px) { .update-item { grid-template-columns: 1fr; } }
---

<div class="update-list">
{% for post in site.posts %}
  <article class="update-item">
    <a href="{{ post.url | relative_url }}" aria-label="{{ post.title | escape }}">
      {% include figure.liquid path=post.thumbnail alt=post.title loading="lazy" %}
    </a>
    <div>
      <p class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%B %d, %Y' }}</time></p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.description }}</p>
    </div>
  </article>
{% endfor %}
</div>
