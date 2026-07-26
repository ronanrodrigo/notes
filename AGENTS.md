# AGENTS.md - Instruções para Agentes de IA

Este documento descreve a estrutura, convenções e instruções operacionais para agentes de IA que trabalham com este repositório.

## Tech Stack

- **Language**: Markdown + YAML (front matter)
- **Hosting**: GitHub Pages com tema Jekyll Cayman
- **Repository**: https://github.com/ronanrodrigo/raycast-notes-backup
- **Site**: https://ronanrodrigo.dev/raycast-notes-backup

## Directory Structure

```
raycast-notes-backup/
├── AGENTS.md                    # Este arquivo (instruções para agentes)
├── README.md                    # Índice de notas e descrição geral
├── index.md                     # Homepage com front matter Jekyll
├── _config.yml                  # Configuração Jekyll (tema cayman)
└── notes/
    ├── 2026-07-26-agentes-ia-pesquisa-automacao.md
    ├── 2026-07-25-omniroute-gateway-ia.md
    ├── 2026-07-25-ferramentas-ia-open-source.md
    ├── 2026-07-24-ferramentas-claude-avancadas.md
    ├── 2026-07-24-colibri-motor-local-ia.md
    ├── 2026-07-23-turbovec-turboquant.md
    ├── 2026-07-23-prompts-claude-aprender-rapido.md
    ├── 2026-07-23-ciclo-criado-pela-ia.md
    ├── 2026-07-23-wellhub-requests.md
    ├── 2026-07-23-pr-visual-evidence.md
    ├── 2026-07-23-assistento-skill-pessoal.md
    ├── 2026-07-23-repos-ia-github-trending.md
    ├── 2026-07-23-trilhas-cursos-ia.md
    └── 2026-07-23-self-host-ia-coolify-agentes-rag.md
```

**Princípio fundamental**: Todas as notas vivem em `notes/` sem subcategorias temáticas. Zero subpastas dentro de `notes/`. Estrutura completamente plana.

## Conventions

### Nomenclatura de Arquivo

**Padrão**: `YYYY-MM-DD-slug.md`

Onde:
- **YYYY-MM-DD**: Data de criação da nota (extraída do título H1 do arquivo, não do commit)
- **slug**: Identificador em kebab-case, sem acentos, sem caracteres especiais, máximo ~50 caracteres
  - Exemplos bons: `self-host-ia-coolify-agentes-rag`, `trilhas-cursos-ia`, `omniroute-gateway-ia`
  - Evitar: `Self Host IA`, `trilhas_cursos`, `omniRoute`, `OmniRoute`

### Conteúdo de Nota

Cada arquivo começa com um título H1 que inclui a data no formato DD/MM/YYYY:

```markdown
# 23/07/2026 - Self-host IA: Coolify, agentes e RAG
```

Esta data é a fonte da verdade para extrair o prefixo YYYY-MM-DD do nome do arquivo. O H1 deve estar presente em todas as notas.

### Links de Arquivo

Ao linkar para uma nota em `index.md`, `README.md` ou outros documentos, use o padrão:

```markdown
[23/07/2026 - Self-host IA: Coolify, agentes e RAG](notes/2026-07-23-self-host-ia-coolify-agentes-rag.md)
```

O formato do link é sempre relativo a partir da raiz (`notes/...`).

## Important Files

| Arquivo | Responsabilidade |
|---------|------------------|
| `index.md` | Homepage com tema Jekyll, front matter, índice de notas em ordem cronológica decrescente |
| `README.md` | Mesmo índice do `index.md` mas sem front matter Jekyll, inclui seção "Sobre" explicando convenções |
| `AGENTS.md` | Este arquivo com instruções, convenções e boundaries para agentes de IA |
| `_config.yml` | Configuração Jekyll (tema cayman, permalinks, domínio customizado) — **não modificar** |
| `notes/*` | Arquivos de notas com padrão YYYY-MM-DD-slug.md — todo conteúdo fica aqui |

## Common Pitfalls

### 1. Linkar com caminho errado
❌ **Errado**: `[Nota](2026-07-23-self-host-ia-coolify-agentes-rag.md)`  
✅ **Certo**: `[Nota](notes/2026-07-23-self-host-ia-coolify-agentes-rag.md)`

### 2. Criar subcategorias dentro de notes/
❌ **Errado**: `notes/ia/2026-07-23-self-host.md`, `notes/tools/turbovec.md`  
✅ **Certo**: `notes/2026-07-23-self-host-ia-coolify-agentes-rag.md`, `notes/2026-07-23-turbovec-turboquant.md`

### 3. Usar data do commit em vez da data do H1
❌ **Errado**: Arquivo criado em 26/07 mas contém H1 "23/07/2026 - ..." → usar `2026-07-26-*`  
✅ **Certo**: Usar `2026-07-23-*` porque o H1 diz que a nota é de 23/07

### 4. Esquecer o H1 com data
❌ **Errado**: Arquivo sem H1 ou com H1 sem data  
✅ **Certo**: Sempre começar com `# DD/MM/YYYY - Título`

### 5. Reordenar notas em index.md/README.md manualmente
❌ **Errado**: Listar notas em ordem alfabética ou aleatória  
✅ **Certo**: Manter ordem cronológica decrescente (mais recente primeiro)

## Status do Repositório

**Última atualização**: 26/07/2026

**Estrutura**: Reorganizada para padrão YYYY-MM-DD na pasta `notes/` (plano, sem categorias temáticas).

**GitHub Pages**: Ativo em https://ronanrodrigo.dev/raycast-notes-backup com tema Jekyll Cayman.

**Total de notas**: 14 arquivos em `notes/`.

## Commands

### Listar todas as notas
```bash
ls -la notes/
```

### Verificar se há subcategorias em notes/ (deve estar vazio)
```bash
find notes/ -mindepth 1 -type d
# Esperado: nenhuma saída (zero subpastas)
```

### Validar formato de nome de arquivo
```bash
# Todos em notes/ devem seguir YYYY-MM-DD-slug.md
ls notes/ | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+\.md$'
```

## Code Style

- **Markdown**: CommonMark com suporte a Jekyll front matter
- **Front matter**: Apenas em `index.md` (não em notas)
- **Links**: Sempre relativo à raiz do repo (`notes/...`, não `./notes/...`)
- **Cabeçalhos**: H1 com data no formato DD/MM/YYYY em cada nota
- **Nomes de arquivo**: kebab-case, sem acentos, sem underscore, sem CamelCase

## Boundaries

Agentes **podem**:
- ✅ Criar, mover, renomear ou deletar arquivos em `notes/`
- ✅ Atualizar `index.md`, `README.md` e `AGENTS.md`
- ✅ Seguir o padrão YYYY-MM-DD-slug.md rigorosamente
- ✅ Reordenar notas em `index.md` e `README.md` por data decrescente
- ✅ Atualizar datas e status neste arquivo

Agentes **não podem**:
- ❌ Criar subcategorias ou subpastas em `notes/`
- ❌ Modificar `_config.yml`
- ❌ Modificar o tema Jekyll ou domínio customizado
- ❌ Quebrar links de notas em `index.md` ou `README.md`
- ❌ Remover o H1 com data de qualquer nota
- ❌ Usar acentos ou caracteres especiais em nomes de arquivo

## Git Workflow

- **Branch padrão**: `main`
- **Commits**: Use mensagens descritivas, ex. `chore: reorganizar nota para padrão YYYY-MM-DD`
- **Pull Requests**: Não obrigatório para pequenas correções em `notes/`, mas recomendado para mudanças estruturais
- **Operação via API**: Prefira `mcp_github_*` tools para criar, editar e deletar arquivos

## Para Claude Code

Quando trabalhando com este repo via Claude Code ou assistentes similares:

1. **Sempre respeitar o padrão YYYY-MM-DD-slug.md**
2. **Manter `notes/` plano** — nunca criar subpastas
3. **Atualizar `index.md` e `README.md`** quando adicionar/remover notas
4. **Verificar links** antes de fazer commit
5. **Manter conteúdo original intacto** ao mover/renomear notas
6. **Usar data do H1 como prefixo** — nunca usar data do commit

## Exemplos de Operações

### Adicionar nova nota
```bash
# 1. Criar arquivo em notes/ com padrão YYYY-MM-DD-slug.md
echo "# 26/07/2026 - Novo Tópico" > notes/2026-07-26-novo-topico.md

# 2. Adicionar link em index.md e README.md (ordem cronológica decrescente)

# 3. Commit e push
```

### Mover nota (cambiar de data)
```bash
# Se a nota tem H1 "# 25/07/2026 - Tópico" mas está em 2026-07-26-*
# 1. Renomear: 2026-07-26-topico.md → 2026-07-25-topico.md
# 2. Atualizar links em index.md e README.md
```

### Deletar nota obsoleta
```bash
# 1. Remover arquivo de notes/
# 2. Remover link de index.md e README.md
# 3. Commit e push
```
