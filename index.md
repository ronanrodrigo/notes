---
layout: page
---

<section class="post-index" aria-labelledby="post-index-title">
  <div class="section-heading">
    <p class="eyebrow">arquivo de notas</p>
    <h1 id="post-index-title">Todas as notas</h1>
  </div>

  <div class="post-grid">
    {% for post in site.posts %}
    <article class="post-card">
      <div class="post-card-header">
        <span class="post-card-index">{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span>
        <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%d/%m/%Y" }}</time>
      </div>

      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>

      <dl class="frontmatter-list">
        {% for field in post.data %}
          {% assign field_name = field[0] %}
          {% assign field_value = field[1] %}
          {% unless field_name == 'layout' or field_name == 'title' or field_name == 'date' %}
          <div class="frontmatter-item">
            <dt>{{ field_name }}</dt>
            <dd>
              {% if field_value contains ' ' or field_value.first %}
                {% if field_value.first %}
                  {% for value in field_value %}<span class="tag">{{ value }}</span>{% unless forloop.last %} {% endunless %}{% endfor %}
                {% else %}
                  {{ field_value }}
                {% endif %}
              {% else %}
                {{ field_value }}
              {% endif %}
            </dd>
          </div>
          {% endunless %}
        {% endfor %}
      </dl>

      <a class="post-card-link" href="{{ post.url | relative_url }}">ler nota <span aria-hidden="true">↗</span></a>
    </article>
    {% endfor %}
  </div>
</section>

<p class="tags-index-link"><a href="{{ '/tags/' | relative_url }}">Ver índice completo de tags →</a></p>
