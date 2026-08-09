---
title: "AGENTS.md - Instruções Oficiais de Criação"
tags:
  - ai-agents
  - github
  - ai
  - tools
  - automation
  - design-systems
  - local-llm
  - testing
  - mobile
date: "2026-07-23"
description: 'Boas práticas oficiais para criar arquivos AGENTS.md úteis para agentes de IA.'
---


Instruções compiladas de fontes oficiais: GitHub Copilot, OpenAI Codex, Claude Code, Cursor e outros agentes de IA.

---

## O que é AGENTS.md?

Um arquivo Markdown na raiz do repositório que serve como **README para agentes de IA**. Define contexto, instruções e preferências que o agente precisa para trabalhar efetivamente no projeto.

**Suportado por**: GitHub Copilot, Claude Code, OpenAI Codex, Cursor, Aider, e outras ferramentas de IA.

---

## Estrutura Recomendada

**Tamanho ideal**: 100-200 linhas (máximo 300)

### 1. **Project Overview** (Obrigatório)

Uma frase descrevendo o projeto usando Stack técnico com versões

### 2. **Tech Stack** (Obrigatório)

Seja específico com versões

### 3. **Build & Test Commands** (Obrigatório - maior impacto)

CRÍTICO: Coloque aqui ANTES de qualquer coisa.

### 4. **Project Structure** (Recomendado)

Organize como:
- Diretórios principais
- Organização de código
- Convenções de nomenclatura

### 5. **Code Style & Conventions** (Recomendado)

Use exemplos reais, NÃO explicações abstratas

### 6. **Boundaries (Always / Ask First / Never)** (Obrigatório)

Defina o que o agente pode fazer livremente, o que requer aprovação, e o que é proibido

### 7. **Testing Requirements** (Recomendado)

- Framework utilizado
- Cobertura esperada
- Localização dos testes

### 8. **Git Workflow** (Recomendado)

- Padrão de commit (Conventional Commits)
- Estratégia de branches
- Process de PR

### 9. **Critical Files & Entry Points** (Opcional)

- Arquivo principal
- Configurações importantes
- Definições de tipos

### 10. **Common Gotchas** (Recomendado)

Problemas comuns que o agente deve evitar

---

## Onde Colocar

- **Preferido**: Raiz do repositório `/AGENTS.md` (maiúsculo)
- **Alternativas**: `/agents.md`, `/.well-known/agents.md`, `/docs/AGENTS.md`
- **Monorepos**: Arquivo raiz + arquivos aninhados em cada package

---

## Dicas Oficiais

✅ **FAÇA:**
- Coloque comandos ANTES de explicações
- Use exemplos reais do seu código
- Seja específico (versões, flags completas)
- Mantenha sob 200 linhas
- Atualize quando a estrutura mudar

❌ **NÃO FAÇA:**
- Descrições vagas
- Comandos sem flags
- Explicações abstratas (use snippets reais)
- Deixar ficar > 300 linhas
- Copiar exemplos de outros projetos

---

## Validação

Use a ferramenta oficial: [Acesse aqui](https://agent-ready.dev)

Seu AGENTS.md deve ter pelo menos **2 de 3**:
- ✅ Comandos de instalação/build/teste
- ✅ Detalhes de configuração
- ✅ Exemplos de uso

---

## Fontes Oficiais

- [Acesse aqui](https://github.com/agentsmd/agents.md) (especificação aberta)
- [Acesse aqui](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) (GitHub oficial)
- [Acesse aqui](https://docs.github.com/en/copilot/reference/custom-agents-configuration) (GitHub Copilot docs)
- [Acesse aqui](https://agent-ready.dev/how-to-write-an-effective-agents-md) (Agent Ready)
- [Acesse aqui](https://developers.openai.com/codex/guides/agents-md.md) (OpenAI Codex)
