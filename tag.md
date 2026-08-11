---
layout: default
title: Posts por tag
permalink: /tag/
---

<section class="tag-page" data-tag-page aria-labelledby="tag-page-title">
  <div class="section-heading">
    <p class="eyebrow">arquivo filtrado</p>
    <h1 id="tag-page-title">Escolha uma tag</h1>
    <p class="section-intro" id="tag-page-description">Selecione uma tag para ver as notas relacionadas.</p>
  </div>

  <p class="tag-page-meta" id="tag-page-meta" aria-live="polite"></p>
  <p class="tag-page-empty" id="tag-page-empty">Nenhuma tag foi selecionada. Volte ao índice para escolher um assunto.</p>

  <div class="post-grid tag-post-grid">
    {% for post in site.posts %}
    <article class="post-card" data-tag-post hidden>
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
        {% for post_tag in post.tags %}
          <a class="tag" data-post-tag="{{ post_tag | slugify }}" data-tag-label="{{ post_tag }}" href="{{ '/tag/' | relative_url }}?tag={{ post_tag | slugify }}">#{{ post_tag }}</a>
        {% endfor %}
      </div>
      {% endif %}

      <a class="post-card-link" href="{{ post.url | relative_url }}">ler nota <span aria-hidden="true">↗</span></a>
    </article>
    {% endfor %}
  </div>

  <p class="tag-page-nav"><a href="{{ '/list-tags/' | relative_url }}">← voltar ao índice de tags</a></p>
</section>

<script>
  (() => {
    const page = document.querySelector('[data-tag-page]');
    if (!page) return;

    const cards = [...page.querySelectorAll('[data-tag-post]')];
    const title = page.querySelector('#tag-page-title');
    const description = page.querySelector('#tag-page-description');
    const meta = page.querySelector('#tag-page-meta');
    const empty = page.querySelector('#tag-page-empty');
    const requestedTag = new URLSearchParams(window.location.search).get('tag');
    const tagSlug = requestedTag ? requestedTag.trim().toLowerCase() : '';

    const matchingCards = tagSlug
      ? cards.filter((card) => [...card.querySelectorAll('[data-post-tag]')]
        .some((tag) => tag.dataset.postTag === tagSlug))
      : [];

    cards.forEach((card) => {
      card.hidden = !matchingCards.includes(card);
    });

    matchingCards.forEach((card, index) => {
      const cardIndex = card.querySelector('.post-card-index');
      if (cardIndex) cardIndex.textContent = String(index + 1).padStart(2, '0');
    });

    if (matchingCards.length > 0) {
      const selectedTag = matchingCards[0].querySelector('[data-post-tag="' + tagSlug + '"]');
      const label = selectedTag ? selectedTag.dataset.tagLabel : requestedTag;
      const count = matchingCards.length;
      title.textContent = '#' + label;
      description.textContent = 'Notas relacionadas a este assunto, da mais recente para a mais antiga.';
      meta.textContent = count + (count === 1 ? ' nota encontrada' : ' notas encontradas');
      empty.hidden = true;
      document.title = '#' + label + ' · ' + document.title;
    }
  })();
</script>
