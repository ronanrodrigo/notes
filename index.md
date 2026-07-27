---
layout: page
---

{% for note in site.notes reversed %}
- [{{ note.date | date: "%d/%m/%Y" }} - {{ note.title }}]({{ note.url | relative_url }})
{% endfor %}

## Índice por Tags

[Ver índice completo de tags]({{ '/tags/' | relative_url }})
