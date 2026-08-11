---
layout: page
---

<aside class="agent-notice" aria-labelledby="agent-notice-title">
  <p class="eyebrow">recursos de navegação</p>

  <h2 id="agent-notice-title">
    Guia de navegação para agentes e leitores automatizados
  </h2>

  <p>
    Para entender a estrutura deste site e descobrir seu conteúdo, consulte o
    <a href="{{ '/agent/' | relative_url }}">guia para agentes de IA</a>.
    Também estão disponíveis o
    <a href="{{ '/llms.txt' | relative_url }}">índice em texto para agentes</a>,
    o
    <a href="{{ '/index.json' | relative_url }}">índice estruturado em JSON</a>,
    o
    <a href="{{ '/sitemap.md' | relative_url }}">mapa do site em Markdown</a>
    e o
    <a href="{{ '/list-tags/' | relative_url }}">índice de tags</a>.
  </p>

  <p>
    Esses recursos são somente para leitura e complementam a navegação normal
    pelas notas publicadas nesta página. Cada nota também possui uma versão
    Markdown limpa em uma URL terminada em <code>.md</code>.
  </p>
</aside>

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

      {% if post.description %}
      <p class="post-card-description">{{ post.description }}</p>
      {% endif %}

      {% if post.tags and post.tags.size > 0 %}
      <div class="post-card-tags" aria-label="Tags desta nota">
        {% for tag in post.tags %}
          <a class="tag" href="{{ '/tag/' | relative_url }}?tag={{ tag | slugify }}">#{{ tag }}</a>
        {% endfor %}
      </div>
      {% endif %}

      <dl class="frontmatter-list">
        {% for field in post.data %}
          {% assign field_name = field[0] %}
          {% assign field_value = field[1] %}
          {% unless field_name == 'layout' or field_name == 'title' or field_name == 'date' or field_name == 'description' or field_name == 'tags' %}
          <div class="frontmatter-item">
            <dt>{{ field_name }}</dt>
            <dd>{{ field_value }}</dd>
          </div>
          {% endunless %}
        {% endfor %}
      </dl>

      <a class="post-card-link" href="{{ post.url | relative_url }}">ler nota <span aria-hidden="true">↗</span></a>
      <a class="post-card-link" href="{{ post.slug | prepend: '/' | append: '.md' | relative_url }}">versão Markdown <span aria-hidden="true">↗</span></a>
    </article>
    {% endfor %}
  </div>
</section>

<p class="tags-index-link"><a href="{{ '/list-tags/' | relative_url }}">Ver índice completo de tags →</a></p>
