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

<section class="tag-index" aria-label="Índice de tags">
  <div class="section-heading">
    <p class="eyebrow">taxonomia das notas</p>
    <p class="section-intro">Explore as notas por assunto. Cada tag abre uma página com os posts relacionados.</p>
  </div>

  <ul class="tag-grid">
    {% for tag in all_tags %}
      {% assign tag_count = 0 %}
      {% for post in site.posts %}
        {% if post.tags contains tag %}
          {% assign tag_count = tag_count | plus: 1 %}
        {% endif %}
      {% endfor %}
      {% if tag_count >= 2 %}
      <li class="tag-index-item">
        <a class="tag-index-link" href="{{ '/tag/' | relative_url }}?tag={{ tag | slugify }}">
          <span class="tag-index-name">#{{ tag }}</span>
          <span class="tag-index-count">{{ tag_count }} {% if tag_count == 1 %}nota{% else %}notas{% endif %} <span aria-hidden="true">↗</span></span>
        </a>
      </li>
      {% endif %}
    {% endfor %}
  </ul>

  <p class="tag-index-note">Exibindo tags usadas em pelo menos duas notas.</p>
</section>
