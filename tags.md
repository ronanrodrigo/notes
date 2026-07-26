---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign all_tags = "" | split: "," %}
{% for note in site.notes %}
  {% if note.tags %}
    {% for tag in note.tags %}
      {% assign all_tags = all_tags | push: tag | uniq %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign all_tags = all_tags | uniq | sort %}

{% for tag in all_tags %}
  {% if tag != "" %}
## {{ tag }}

{% assign tagged_notes = site.notes | where_exp: "note", "note.tags contains tag" %}
{% for note in tagged_notes reversed %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url }})
{% endfor %}

  {% endif %}
{% endfor %}
