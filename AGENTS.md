# AGENTS.md

> Repositório de posts em Markdown, renderizado como site Jekyll no GitHub Pages.

## Stack

- **Linguagem**: Markdown
- **Versionamento**: Git + GitHub
- **Renderização**: Jekyll + remote theme
- **Automação**: índices gerados no próprio site via Liquid, sem workflow custom para isso

## Estrutura do projeto

- `_posts/` — posts individuais em Markdown com frontmatter
- `index.md` — índice principal do site
- `tags.md` — índice por tags
- `_layouts/post.html` — layout aplicado aos posts
- `_config.yml` — configuração do Jekyll

## Frontmatter padrão

Todo post deve começar com YAML frontmatter válido:

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

O nome do arquivo deve seguir o padrão `YYYY-MM-DD-slug.md`. A data do nome deve ser compatível com a data do frontmatter.

## Regras de tags

- Minúsculas
- Kebab-case
- Sem acentos
- Pelo menos 2 tags por post

## Convenções

- Manter posts dentro de `_posts/`
- Não editar manualmente as listas de `index.md` e `tags.md`; elas são renderizadas por Jekyll
- Usar Markdown puro

## Git workflow

1. Criar ou editar posts em `_posts/`
2. Fazer commit em uma branch de trabalho
3. Abrir um pull request para `main`
4. O GitHub Pages renderiza o site automaticamente após a integração

## Não fazer

- Não remover frontmatter
- Não criar automação custom para atualizar índices
- Não usar formatos fora de Markdown
- Não criar uma collection customizada `notes`
