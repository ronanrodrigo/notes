# AGENTS.md

> Repositório de notas em formato Markdown. Armazenar e gerenciar notas pessoais sobre IA, infraestrutura, desenvolvimento e tecnologia.

## Tech Stack

- **Linguagem**: Markdown
- **Versionamento**: Git + GitHub
- **Estrutura**: Notas soltas em `notes/` ordenadas por data (YYYY-MM-DD-slug.md)
- **Formato**: Markdown plano com YAML frontmatter
- **Automação**: GitHub Actions para atualizar índice automaticamente

## Project Overview

Este repositório é um backup privado de notas convertidas para formato Markdown. Cada nota é armazenada como um arquivo separado para fácil navegação, busca e controle de versão.

**Tópicos principais**:
1. Self-host IA: Coolify, agentes e RAG
2. Trilhas e cursos de IA
3. Repos de IA (GitHub Trending)
4. Assistento - Skill Pessoal
5. PR Visual Evidence
6. Wellhub requests
7. Ciclo criado pela IA
8. YouTube Prompts e Estratégia de Canal
9. Claude Tools e Plugins

## Directory Structure

```
notes/
├── AGENTS.md                          # Este arquivo
├── README.md                          # Índice de notas (atualizado automaticamente)
├── index.md                           # Página inicial para GitHub Pages
├── .github/workflows/
│   └── update-notes-index.yml        # GitHub Action para atualizar índice
└── notes/                             # Diretório principal de notas
    ├── 2026-07-23-*.md               # Notas com frontmatter e tags
    ├── 2026-07-24-*.md
    ├── 2026-07-25-*.md
    └── 2026-07-26-*.md
```

## Frontmatter & Tags

### Estrutura obrigatória

Toda nota DEVE começar com YAML frontmatter no seguinte formato:

```yaml
---
title: Título descritivo da nota
date: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
---

# Data DD/MM/YYYY - Título da Nota

Conteúdo da nota aqui...
```

### Regras de Tags

- **Obrigatórias**: Toda nota deve ter pelo menos 2 tags
- **Formato**: Minúsculas, separadas por hífen (kebab-case), sem acentos
- **Quantidade recomendada**: 3-8 tags por nota
- **Objetivo**: Facilitar buscas, filtros e categorização

### Exemplo de nota completa

```yaml
---
title: YouTube - Prompts e Estratégia para Crescimento
date: 2026-07-26
tags:
  - youtube
  - content-creation
  - prompts
  - growth-strategy
  - shorts
  - monetization
  - seo
---

# 26/07/2026 - YouTube: Prompts e Estratégia para Crescimento de Canal

## Seção 1
...
```

### Tags Padrão (não exaustivo)

| Categoria | Tags |
|-----------|------|
| **IA** | `ia`, `llm`, `claude`, `chatgpt`, `open-source`, `modelos-locais` |
| **Desenvolvimento** | `development`, `backend`, `frontend`, `devops`, `rust`, `python`, `javascript` |
| **Agentes** | `agentes`, `bot`, `automation`, `workflow` |
| **Plataformas** | `github`, `github-actions`, `docker`, `kubernetes`, `cloud` |
| **Conteúdo** | `youtube`, `content-creation`, `shorts`, `prompts`, `seo` |
| **Integração** | `integrations`, `apis`, `mcp`, `plugins`, `tools` |
| **Aprendizado** | `learning`, `course`, `tutorial`, `documentation` |

**Dica**: Use tags genéricas (ex: `ia`, `development`) + específicas (ex: `claude`, `rust`)

## Commands

### Setup
```bash
# Clonar repositório
git clone git@github.com:ronanrodrigo/notes.git
cd notes
```

### Viewing & Searching
```bash
# Listar todas as notas
ls -la notes/

# Buscar por conteúdo
grep -r "termo-buscado" notes/

# Buscar por tag
grep -r "tags:" notes/ | grep "tag-buscada"

# Visualizar uma nota específica
cat notes/2026-07-23-self-host-ia-coolify-agentes-rag.md
```

### Contributing
```bash
# Criar branch de feature
git checkout -b feature/nova-nota

# Criar nova nota com frontmatter
# ... editar arquivo markdown com frontmatter obrigatório

# Commit usando Conventional Commits
git add notes/
git commit -m "feat: adicionar nova nota sobre tema"

# Push - GitHub Action atualiza README.md e index.md automaticamente
git push origin feature/nova-nota

# Criar Pull Request no GitHub
```

## Code Style & Conventions

### Markdown Formatting

**Good Example** - Estrutura clara e hierárquica com frontmatter:
```markdown
---
title: Título da Nota
date: YYYY-MM-DD
tags:
  - tag1
  - tag2
---

# Título Principal

## Seção 1

### Subseção 1.1

- Item 1
- Item 2

**Destaque importante**: Usar negrito para conceitos-chave

> Citações ou notas importantes em blockquote

```code
Blocos de código quando necessário
```
```

**Anti-pattern** - Evitar:
```markdown
sem frontmatter
# titulo em lowercase
sem hierarquia clara
tudo misturado num único parágrafo
sem tags
```

### Conventions

- **Nomes de arquivo**: Use kebab-case com prefixo numérico (YYYY-MM-DD-slug.md)
- **Frontmatter**: OBRIGATÓRIO no início do arquivo com `title`, `date`, `tags`
- **Títulos**: Use H1 (#) para título principal, H2 (##) para seções
- **Links**: Use links relativos (`notes/arquivo.md`)
- **Listas**: Use `-` para bullets, `1.` para listas numeradas
- **Ênfase**: Use `**bold**` para conceitos importantes, `_italic_` para termos estrangeiros
- **Blocos de código**: Use ``` com linguagem especificada

## GitHub Actions - Automação de Índice

O repositório possui um GitHub Action que roda automaticamente toda vez que um arquivo `.md` é criado ou modificado em `notes/`:

- ✅ Lê todas as notas de `notes/`
- ✅ Extrai data do nome do arquivo e título do frontmatter
- ✅ Ordena por data (mais recentes primeiro)
- ✅ Atualiza `README.md` entre os marcadores `<!-- NOTES_INDEX_START -->` e `<!-- NOTES_INDEX_END -->`
- ✅ Também atualiza `index.md` para o site
- ✅ Faz commit automático com mensagem `docs: update notes index`

**Você não precisa fazer nada** - o índice é atualizado automaticamente!

## Boundaries

### Always
- Adicionar frontmatter com `title`, `date`, `tags` em toda nota nova
- Colocar tags em kebab-case, minúsculas, sem acentos
- Usar pelo menos 2 tags por nota
- Modificar/adicionar notas dentro do diretório `notes/`
- Usar Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`
- Manter nomenclatura consistente YYYY-MM-DD-slug.md
- Usar Markdown plano com YAML frontmatter

### Ask First
- Mudanças na estrutura do repositório
- Adicionar novas automações ou dependências externas
- Mudanças no GitHub Action de índice

### Never
- Commit de dados pessoais ou sensíveis
- Notas sem frontmatter
- Notas sem tags
- Usar formatação proprietária (não-Markdown)
- Commit de arquivos binários grandes
- Deletar notas sem documentar
- Modificar README.md ou index.md manualmente (são atualizados por Action)

## Git Workflow

1. `git checkout -b feature/nome-descritivo`
2. Criar ou editar notas em `notes/` **com frontmatter e tags**
3. `git commit -m "feat: descrição clara"`
4. `git push origin feature/nome-descritivo` (GitHub Action atualiza índices automaticamente)
5. Criar Pull Request e merge na `main`

## Important Files

- **README.md** - Índice de todas as notas (atualizado automaticamente)
- **index.md** - Página inicial para site (atualizado automaticamente)
- **AGENTS.md** - Este arquivo
- **.github/workflows/update-notes-index.yml** - GitHub Action de automação
- **notes/** - Diretório com todas as notas em Markdown

## Common Pitfalls

### Nota criada sem frontmatter
**Solução**: Adicionar YAML frontmatter no início com `title`, `date`, `tags`

### Esquecer de adicionar tags
**Solução**: Toda nota precisa de pelo menos 2 tags para findability

### Índice não atualiza
**Solução**: GitHub Action roda automaticamente. Verifique em Actions se houve erro. Se não houve erro, use `git pull` localmente para atualizar.

### Links quebrados após renomear
**Solução**: README.md é gerado automaticamente, então não precisa atualizar manualmente

### Clone errado de repositório
**Solução**: Usar `git clone git@github.com:ronanrodrigo/notes.git`

## Status do Repositório

- **Tipo**: Private repository
- **Branch padrão**: `main`
- **Site**: https://ronanrodrigo.dev/notes
- **Automação**: GitHub Actions (update-notes-index.yml)
- **Deploy**: Automático via GitHub Pages

## Para Claude Code

```bash
cp AGENTS.md CLAUDE.md
```
