---
layout: page
title: Tags
permalink: /list-tags/
---

{% assign all_tags = '' | split: '' %}
{% for post in site.posts %}
  {% for tag in post.tags %}
    {% assign all_tags = all_tags | push: tag %}
  {% endfor %}
{% endfor %}

{% assign all_tags = all_tags | uniq | sort %}

<ul>
{% for tag in all_tags %}
  {% assign tag_count = 0 %}
  {% for post in site.posts %}
    {% if post.tags contains tag %}
      {% assign tag_count = tag_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  {% if tag_count >= 2 %}
    <li>{{ tag }}</li>
  {% endif %}
{% endfor %}
</ul>
