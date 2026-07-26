---
layout: page
title: Notas
---

Notas organizadas por data no repositório privado.

## Índice de Notas

{% assign notes = site.pages | where_exp: "item", "item.path contains 'notes/' and item.date" | sort: "date" | reverse %}

{% for note in notes %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url }})
{% endfor %}

## Índice por Tags

[Ver índice completo de tags](/tags/)
