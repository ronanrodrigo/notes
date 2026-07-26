---
layout: page
title: Índice por Tags
permalink: /tags/
---

{% assign notes = site.pages | where_exp: "item", "item.path contains 'notes/' and item.date" %}
{% capture raw_tags %}{% for note in notes %}{% if note.tags %}{% for tag in note.tags %}{{ tag }}|{% endfor %}{% endif %}{% endfor %}{% endcapture %}
{% assign all_tags = raw_tags | split: '|' | uniq | sort %}

{% for tag in all_tags %}
{% assign current_tag = tag | strip %}
{% if current_tag != blank %}
<h2 id="{{ current_tag | slugify }}">{{ current_tag }}</h2>

{% assign tagged_notes = notes | where_exp: "item", "item.tags contains current_tag" | sort: "date" | reverse %}
{% for note in tagged_notes %}
* [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url | relative_url }})
{% endfor %}

{% endif %}
{% endfor %}
