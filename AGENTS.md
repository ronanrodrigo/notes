# AGENTS.md

> Backup privado de Raycast Notes em formato Markdown. Um repositório para armazenar e gerenciar notas pessoais sobre IA, infraestrutura, desenvolvimento e tecnologia.

## Tech Stack

- **Linguagem**: Markdown
- **Versionamento**: Git + GitHub
- **Estrutura**: Notas organizadas por tópico
- **Formato**: Markdown plano (sem dependências externas)

## Project Overview

Este repositório é um backup privado de todas as Raycast Notes convertidas para formato Markdown. Cada nota é armazenada como um arquivo separado para fácil navegação, busca e controle de versão.

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
raycast-notes-backup/
├── AGENTS.md                          # Este arquivo
├── README.md                          # Índice de notas
└── notes/                             # Diretório principal de notas
    ├── 01-self-host-ia-coolify-agentes-rag.md
    ├── 02-trilhas-cursos-ia.md
    ├── 03-repos-ia-github-trending.md
    ├── 04-assistento-skill-pessoal.md
    ├── 05-pr-visual-evidence.md
    ├── 06-wellhub-requests.md
    └── 07-ciclo-criado-pela-ia.md
```

## Commands

### Setup
```bash
# Clonar repositório
git clone git@github.com:ronanrodrigo/raycast-notes-backup.git
cd raycast-notes-backup
```

### Viewing & Searching
```bash
# Listar todas as notas
ls -la notes/

# Buscar por conteúdo
grep -r "termo-buscado" notes/

# Visualizar uma nota específica
cat notes/01-self-host-ia-coolify-agentes-rag.md
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

\`\`\`code
Blocos de código quando necessário
\`\`\`
```

**Anti-pattern** - Evitar:
```markdown
# titulo em lowercase
sem hierarquia clara
tudo misturado num único parágrafo sem estrutura nem separação
```

### Conventions

- **Nomes de arquivo**: Use kebab-case com prefixo numérico (`01-nome-descritivo.md`)
- **Títulos**: Use H1 (#) para título principal, H2 (##) para seções
- **Links**: Use links relativos quando possível (`../notes/outro-arquivo.md`)
- **Listas**: Use `-` para bullets, `1.` para listas numeradas
- **Ênfase**: Use `**bold**` para conceitos importantes, `_italic_` para termos estrangeiros
- **Blocos de código**: Use ` ``` ` com linguagem especificada quando aplicável
- **Referências**: Cite fontes com links quando apropriado

## Boundaries

### Always
- Modificar/adicionar notas dentro do diretório `/notes`
- Usar Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`
- Manter nomenclatura consistente com prefixo numérico
- Usar Markdown plano (sem HTML ou templates complexos)
- Documentar mudanças no README.md quando adicionar novas notas

### Ask First
- Mudanças na estrutura de diretórios
- Reorganizar ou renomear notas existentes
- Adicionar novas ferramentas ou automações
- Mudar formato de armazenamento
- Adicionar dependências externas

### Never
- Commit de dados pessoais ou sensíveis
- Modificar README.md sem atualizar índice
- Usar formatação proprietária (não-Markdown)
- Adicionar arquivos binários grandes
- Deletar notas sem documentar em commit
- Commit de arquivos `.env` ou secrets

## Git Workflow

1. **Branch**: `git checkout -b feature/nome-descritivo`
2. **Editar**: Adicionar/modificar notas em `/notes`
3. **Commit**: `git commit -m "feat: descrição clara"`
   - `feat:` - Nova nota ou seção
   - `fix:` - Correção de conteúdo
   - `docs:` - Atualização de README/AGENTS.md
   - `chore:` - Reorganização ou formatação
4. **Push**: `git push origin feature/nome-descritivo`
5. **PR**: Criar Pull Request com descrição clara
6. **Merge**: Revisar e fazer merge na `main`

### Conventional Commits Examples
- `feat: adicionar nota sobre self-hosting com Coolify`
- `fix: corrigir links quebrados na nota 03`
- `docs: atualizar índice no README.md`
- `chore: reformatar seções com melhor indentação`

## Important Files

- **README.md** - Índice de todas as notas
- **AGENTS.md** - Instruções para agentes de IA (este arquivo)
- **notes/** - Diretório principal com todas as notas em Markdown

## Common Pitfalls

### Problema: Links quebrados após renomear nota
**Causa**: Referências relativas não foram atualizadas
**Solução**: Buscar todos os links `../notes/` que referenciam o arquivo renomeado e atualizar

**Exemplo correto**:
```bash
grep -r "nome-antigo" notes/
# Atualizar para novo nome
```

### Problema: Arquivo não aparece no README.md
**Causa**: Não adicionado manualmente ao índice
**Solução**: Adicionar entry no README.md com número sequencial e descrição

**Formato correto no README**:
```markdown
8. [Nome da Nota](./notes/08-nome-descritivo.md)
```

## Status do Repositório

- **Tipo**: Private repository
- **Criado**: 23 de julho de 2026
- **Última atualização**: 23 de julho de 2026
- **Branch padrão**: `main`
- **Issues**: 0
- **Pull Requests**: 0

## Para Claude Code

Se estiver usando Claude Code especificamente, copie este arquivo:

```bash
cp AGENTS.md CLAUDE.md
```

E adicione instruções específicas ao final conforme necessário.