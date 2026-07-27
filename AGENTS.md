---
layout: page
title: Instruções para agentes
description: Instruções de desenvolvimento e manutenção do site Jekyll
permalink: /agents.md
---

# AGENTS.md

> Repositório de posts em Markdown, renderizado como site Jekyll no GitHub Pages.

## Objetivo do repositório

Este repositório mantém conteúdos publicados como posts. O Jekyll lê os arquivos de `_posts/`, aplica o front matter e os layouts e gera o site estático. A coleção padrão do projeto é `posts`; não existe uma coleção customizada chamada `notes`.

## Stack

- **Conteúdo**: Markdown com front matter YAML
- **Versionamento**: Git + GitHub
- **Renderização**: Jekyll + GitHub Pages
- **Markdown**: kramdown com sintaxe GFM
- **Syntax highlighting**: Rouge
- **Plugins**: `jekyll-feed` e `jekyll-seo-tag`
- **Listagens**: Liquid usando `site.posts`, sem índices mantidos manualmente

## Estrutura do projeto

- `_posts/` — todos os conteúdos publicáveis, organizados como posts Jekyll
- `index.md` — página inicial, que lista os posts via `site.posts`
- `tags.md` — página de índice por tags
- `_layouts/post.html` — layout aplicado aos posts
- `_config.yml` — configuração do Jekyll
- `.github/workflows/` — automações do GitHub Actions, quando aplicável
- `AGENTS.md` — estas instruções, também publicadas no site

## Criar ou editar um post

Todo conteúdo deve ficar em `_posts/` e começar com front matter YAML válido:

```yaml
---
title: Título descritivo do post
date: YYYY-MM-DD
tags:
  - tag1
  - tag2
layout: post
---
```

O nome do arquivo deve seguir `YYYY-MM-DD-slug.md`. A data do nome deve ser compatível com a data do front matter. Use um slug em minúsculas, legível e separado por hífens.

Antes de criar um post, confira os arquivos existentes em `_posts/` para evitar duplicidade de conteúdo ou de slug. Ao editar um post já publicado, preserve o nome do arquivo e altere a data somente quando isso fizer parte explícita da tarefa.

## Regras de tags

- Usar minúsculas
- Usar kebab-case
- Não usar acentos
- Usar pelo menos 2 tags por post, quando o assunto permitir
- Reutilizar tags existentes sempre que forem semanticamente adequadas

## Convenções de conteúdo

- Usar Markdown puro compatível com kramdown/GFM.
- Manter os conteúdos publicáveis exclusivamente em `_posts/`.
- Não criar nem reintroduzir uma pasta `notes/` para conteúdos.
- Não editar manualmente as listas de `index.md` ou `tags.md`; elas são geradas por Liquid/Jekyll.
- Usar `layout: post` nos posts, salvo quando houver uma necessidade explícita de outro layout.
- Manter o front matter delimitado por `---` e válido em YAML.
- Não publicar instruções internas ou arquivos operacionais como posts.

## Validação

Antes de abrir um pull request:

1. Verifique o caminho e o nome do arquivo (`_posts/YYYY-MM-DD-slug.md`).
2. Confirme a validade do front matter e a compatibilidade entre a data do arquivo e a data declarada.
3. Confira links, código, tags e formatação Markdown.
4. Verifique se a alteração não exige mudanças manuais em `index.md` ou `tags.md`.
5. Se o ambiente local estiver configurado, execute a validação/build do Jekyll e corrija erros de renderização.

## Git workflow

1. Criar ou editar posts em `_posts/`.
2. Fazer commit em uma branch de trabalho com uma mensagem objetiva.
3. Abrir um pull request para `main`.
4. Após a integração, o GitHub Pages renderiza o site automaticamente conforme a configuração do repositório.

## Não fazer

- Não remover o front matter dos posts.
- Não colocar novos conteúdos publicáveis fora de `_posts/`.
- Não criar uma collection customizada `notes`.
- Não renomear `_posts/` para `notes/`.
- Não manter índices duplicados ou atualizar manualmente as listagens geradas por Liquid.
- Não criar automação customizada para substituir o comportamento padrão do Jekyll sem necessidade.
- Não usar formatos de conteúdo incompatíveis com o fluxo Markdown/Jekyll.
