---
layout: page
title: Índice de Notas
---

Notas organizadas por data. O site é renderizado diretamente pelo Jekyll, então qualquer nota nova em `notes/` entra automaticamente na listagem.

[Ver índice por tags]({{ '/tags/' | relative_url }})

{% assign notes = site.pages | where_exp: "item", "item.path contains 'notes/' and item.date" | sort: "date" | reverse %}

{% for note in notes %}
* [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url | relative_url }})
{% endfor %}
