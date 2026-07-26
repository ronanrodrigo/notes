# AGENTS.md

> Repositório de notas em formato Markdown. Armazenar e gerenciar notas pessoais sobre IA, infraestrutura, desenvolvimento e tecnologia.

## Tech Stack

- **Linguagem**: Markdown
- **Versionamento**: Git + GitHub
- **Estrutura**: Notas soltas em `notes/` ordenadas por data (YYYY-MM-DD-slug.md)
- **Formato**: Markdown plano (sem dependências externas)

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

## Directory Structure

```
notes/
├── AGENTS.md                          # Este arquivo
├── README.md                          # Índice de notas
├── index.md                           # Página inicial para GitHub Pages
└── notes/                             # Diretório principal de notas
    ├── 2026-07-23-self-host-ia-coolify-agentes-rag.md
    ├── 2026-07-23-trilhas-cursos-ia.md
    ├── 2026-07-23-repos-ia-github-trending.md
    ├── 2026-07-23-assistento-skill-pessoal.md
    ├── 2026-07-23-pr-visual-evidence.md
    ├── 2026-07-23-wellhub-requests.md
    ├── 2026-07-23-ciclo-criado-pela-ia.md
    ├── 2026-07-23-turbovec-turboquant.md
    ├── 2026-07-23-prompts-claude-aprender-rapido.md
    ├── 2026-07-24-colibri-motor-local-ia.md
    ├── 2026-07-24-ferramentas-claude-avancadas.md
    ├── 2026-07-25-ferramentas-ia-open-source.md
    ├── 2026-07-25-omniroute-gateway-ia.md
    └── 2026-07-26-agentes-ia-pesquisa-automacao.md
```

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

# Visualizar uma nota específica
cat notes/2026-07-23-self-host-ia-coolify-agentes-rag.md
```

### Contributing
```bash
# Criar branch de feature
git checkout -b feature/nova-nota

# Adicionar/modificar notas
# ... editar arquivos markdown

# Commit usando Conventional Commits
git add notes/
git commit -m "feat: adicionar nova nota sobre tema"

# Push
git push origin feature/nova-nota

# Criar Pull Request no GitHub
```

## Code Style & Conventions

### Markdown Formatting

**Good Example** - Estrutura clara e hierárquica:
```markdown
# Título Principal

## Seção 1

### Subseção 1.1

- Item 1
- Item 2

### Subseção 1.2

**Destaque importante**: Usar negrito para conceitos-chave

> Citações ou notas importantes em blockquote

```code
Blocos de código quando necessário
```
```

**Anti-pattern** - Evitar:
```markdown
# titulo em lowercase
sem hierarquia clara
tudo misturado num único parágrafo
```

### Conventions

- **Nomes de arquivo**: Use kebab-case com prefixo numérico (YYYY-MM-DD-slug.md)
- **Títulos**: Use H1 (#) para título principal, H2 (##) para seções
- **Links**: Use links relativos (`notes/arquivo.md`)
- **Listas**: Use `-` para bullets, `1.` para listas numeradas
- **Ênfase**: Use `**bold**` para conceitos importantes, `_italic_` para termos estrangeiros
- **Blocos de código**: Use ``` com linguagem especificada

## Boundaries

### Always
- Modificar/adicionar notas dentro do diretório `notes/`
- Usar Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`
- Manter nomenclatura consistente YYYY-MM-DD-slug.md
- Usar Markdown plano
- Documentar mudanças no README.md

### Ask First
- Mudanças na estrutura do repositório
- Adicionar novas automações ou dependências externas

### Never
- Commit de dados pessoais ou sensíveis
- Modificar README.md sem atualizar índice
- Usar formatação proprietária (não-Markdown)
- Commit de arquivos binários grandes
- Deletar notas sem documentar

## Git Workflow

1. `git checkout -b feature/nome-descritivo`
2. Editar notas em `notes/`
3. `git commit -m "feat: descrição clara"`
4. `git push origin feature/nome-descritivo`
5. Criar Pull Request e merge na `main`

## Important Files

- **README.md** - Índice de todas as notas
- **AGENTS.md** - Este arquivo
- **index.md** - Página inicial para site
- **notes/** - Diretório com todas as notas em Markdown

## Common Pitfalls

### Links quebrados após renomear
**Solução**: Atualizar referências em README.md e index.md

### Clone errado de repositório
**Solução**: Usar `git clone git@github.com:ronanrodrigo/notes.git`

## Status do Repositório

- **Tipo**: Private repository
- **Branch padrão**: `main`
- **Site**: https://ronanrodrigo.dev/notes

## Para Claude Code

```bash
cp AGENTS.md CLAUDE.md
```