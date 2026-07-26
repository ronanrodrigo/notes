---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign notes = site.notes %}
{% capture raw_tags %}{% for note in notes %}{% if note.tags %}{% for tag in note.tags %}{{ tag }}|{% endfor %}{% endif %}{% endfor %}{% endcapture %}
{% assign all_tags = raw_tags | split: '|' | uniq | sort %}

{% for tag in all_tags %}
{% assign current_tag = tag | strip %}
{% if current_tag != blank %}

## {{ current_tag }}

{% assign tagged_notes = notes | where_exp: "item", "item.tags contains current_tag" | sort: "date" | reverse %}
{% for note in tagged_notes %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url }})
{% endfor %}

{% endif %}
{% endfor %}
