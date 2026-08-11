---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign all_tags = '' | split: '' %}
{% for post in site.posts %}
  {% for tag in post.tags %}
    {% assign all_tags = all_tags | push: tag %}
  {% endfor %}
{% endfor %}

{% assign all_tags = all_tags | uniq | sort %}

<p class="section-intro">Índice completo das notas agrupadas por tag.</p>

{% for tag in all_tags %}
  {% assign tag_count = 0 %}
  {% for post in site.posts %}
    {% if post.tags contains tag %}
      {% assign tag_count = tag_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  {% if tag_count >= 2 %}
## [{{ tag }}]({{ '/tag/' | relative_url }}?tag={{ tag | slugify }})

{% for post in site.posts %}
  {% if post.tags contains tag %}
- [{{ post.date | date: "%d/%m/%Y" }} - {{ post.title }}]({{ post.url | relative_url }}){% if post.description %} — {{ post.description }}{% endif %}
  {% endif %}
{% endfor %}

  {% endif %}
{% endfor %}
