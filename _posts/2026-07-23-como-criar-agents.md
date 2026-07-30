---
title: "Como criar um arquivo Agents.md"
tags: [agents, github, ia, documentation, examples]
date: "2026-07-23"
description: 'Estrutura recomendada e exemplos reais para orientar agentes de IA em repositórios.'
---


Instruções reais extraídas de arquivos **AGENTS.md** / **Agents.md** de repositórios conhecidos:

## Exemplos de repositórios famosos que usam o arquivo

- **google/benchmark** → `AGENTS.md`
- **radareorg/radare2** → `AGENTS.md`
- **nextdns/nextdns** → `AGENTS.md`
- **DataDog/stratus-red-team** → `AGENTS.md`
- **PaloAltoNetworks/docusaurus-openapi-docs** → `AGENTS.md`
- **chartbrew/chartbrew** → `AGENTS.md`
- **yanyiwu/nodejieba** → `AGENTS.md`

## Estrutura recomendada (compilada de arquivos reais)

A maioria dos arquivos segue este modelo:

```markdown
# AGENTS

## Project Context
- Project: Nome do projeto
- Language: Linguagem principal
- Purpose: Objetivo do projeto

## Repository Overview
- Breve descrição do repositório
- Licença

## Architecture & Key Paths
- Principais diretórios e o que cada um contém
- Stack técnica (frameworks, linguagens, ferramentas)

## Guidelines for AI Agents
- Regras específicas para agentes de IA (ex: "Ask rather than guess")
- Padrões de código
- Quando criar releases
- Restrições técnicas (ex: "Kotlin only — no Java files")

## Additional Rules
- Regras específicas do projeto (testes, releases, etc.)
```

## Dicas observadas nos repositórios

- O arquivo costuma ficar na raiz do repositório
- Nome mais comum: `AGENTS.md` (maiúsculo) ou `Agents.md`
- Muitos projetos o usam para orientar **GitHub Copilot**, **Claude Code**, **Codex** e outros agentes
- O conteúdo é sempre específico do projeto (não genérico)

## Fontes reais consultadas

- Repositórios listados acima (busca direta no GitHub por `filename:AGENTS.md`)
- Padrão observado em mais de 160 mil resultados de busca no GitHub

---

**Nota**: Estas instruções foram extraídas diretamente dos arquivos existentes, sem invenção.
