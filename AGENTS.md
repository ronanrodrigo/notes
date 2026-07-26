# AGENTS.md

> Repositório de notas em Markdown, renderizado como site Jekyll no GitHub Pages.

## Stack

- **Linguagem**: Markdown
- **Versionamento**: Git + GitHub
- **Renderização**: Jekyll + remote theme
- **Automação**: índices gerados no próprio site via Liquid, sem workflow custom para isso

## Estrutura do projeto

- `notes/` — notas individuais em Markdown com frontmatter
- `index.md` — índice principal do site
- `tags.md` — índice por tags
- `_layouts/note.html` — layout aplicado às notas
- `_config.yml` — configuração do Jekyll

## Frontmatter obrigatório

Toda nota deve começar com YAML frontmatter:

```yaml
---
title: Título descritivo da nota
date: YYYY-MM-DD
tags:
  - tag1
  - tag2
---
```

## Regras de tags

- Minúsculas
- Kebab-case
- Sem acentos
- Pelo menos 2 tags por nota

## Convenções

- Nome de arquivo: `YYYY-MM-DD-slug.md`
- Manter notas dentro de `notes/`
- Não editar manualmente as listas de `index.md` e `tags.md`; elas são renderizadas por Jekyll
- Usar Markdown puro

## Git workflow

1. Criar ou editar notas em `notes/`
2. Fazer commit direto na `main`
3. O GitHub Pages renderiza o site automaticamente

## Não fazer

- Não remover frontmatter
- Não criar automação custom para atualizar índices
- Não usar formatos fora de Markdown
