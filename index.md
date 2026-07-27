---
layout: page
---

{% for post in site.posts %}
- [{{ post.date | date: "%d/%m/%Y" }} - {{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

[Ver índice completo de tags]({{ '/tags/' | relative_url }})
