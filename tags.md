---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign all_tags = '' | split: '' %}
{% for post in site.posts %}
  {% if post.tags %}
    {% for tag in post.tags %}
      {% assign all_tags = all_tags | push: tag | uniq %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign all_tags = all_tags | uniq | sort %}

{% for tag in all_tags %}
  {% if tag != '' %}
## {{ tag }}

{% for post in site.posts %}
  {% if post.tags and post.tags contains tag %}
- [{{ post.date | date: "%d/%m/%Y" }} - {{ post.title }}]({{ post.url | relative_url }}){% if post.description %} — {{ post.description }}{% endif %}
  {% endif %}
{% endfor %}

  {% endif %}
{% endfor %}
