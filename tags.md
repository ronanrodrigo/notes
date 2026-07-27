---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign all_tags = '' | split: '' %}
{% for note in site.notes %}
  {% if note.tags %}
    {% for tag in note.tags %}
      {% assign all_tags = all_tags | push: tag | uniq %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign all_tags = all_tags | uniq | sort %}

{% for tag in all_tags %}
  {% if tag != '' %}
## {{ tag }}

{% for note in site.notes reversed %}
  {% if note.tags and note.tags contains tag %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url | relative_url }})
  {% endif %}
{% endfor %}

  {% endif %}
{% endfor %}