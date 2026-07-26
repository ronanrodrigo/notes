---
layout: page
title: Notas
---

Notas organizadas por data no repositório privado.

## Índice de Notas

{% for note in site.notes reversed %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url }})
{% endfor %}

## Índice por Tags

[Ver índice completo de tags](/tags/)
