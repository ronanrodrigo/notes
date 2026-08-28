---
title: "awesome-gamedev-agent-skills: 68 skills de game dev para agentes de código"
description: "Curadoria de um repositório open-source com 68 Agent Skills de game development e um router que carrega a skill certa por engine e tarefa, mais as fontes primárias do padrão Agent Skills."
date: 2026-08-28
tags:
  - agent-skills
  - ai-agents
  - open-source
  - claude
layout: post
---

## awesome-gamedev-agent-skills

Coleção open-source (Apache-2.0) com 68 Agent Skills de desenvolvimento de jogos e um router que detecta a engine pelo projeto e carrega só as skills pertinentes à tarefa. Cobre Godot (4.7), Unity (6.3 LTS), Unreal (5.8), Phaser, PixiJS, three.js, Bevy, pygame, LÖVE e Roblox. Cada skill é escrita a partir da documentação primária da engine, fixada em uma versão declarada e validada por `scripts/validate-skills.py`. A instalação é um comando (`npx skills add gamedev-skills/awesome-gamedev-agent-skills`); os mesmos arquivos `SKILL.md` carregam nativamente em Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, Kiro e dezenas de clientes.

[Acesse o repositório no GitHub](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)

## Especificação Agent Skills (padrão aberto)

Documento que define o formato portátil `SKILL.md`: frontmatter com `name` (1–64 caracteres, minúsculas, dígitos e hífens) e `description` (até 1024 caracteres, dizendo o quê e quando usar), corpo em Markdown livre e campos opcionais como `license`, `compatibility` e `metadata`. É a referência que o repositório segue para manter os arquivos previsíveis entre clientes.

[Leia a especificação](https://agentskills.io/specification)

## Agent Skills na documentação da Anthropic

Visão oficial do que são Agent Skills: capacidades modulares empacotadas em um diretório com `SKILL.md` contendo instruções e metadados opcionais (scripts, templates). O agente carrega o `SKILL.md` completo em contexto só quando julga a skill relevante, o que mantém o uso de tokens baixo e a curadoria sob demanda.

[Documentação de Agent Skills da Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

## CLI skills (instalador universal)

Pacote npm que detecta o agente em uso e instala skills em um comando (`npx skills add ...`), com flags para escopo global (`-g`), agente-alvo (`-a`) e listagem prévia (`--list`). Suporta mais de 50 clientes — entre eles Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot e Hermes Agent (`.hermes/skills/`) — sem arquivos de regra específicos por editor.

[Veja o pacote no npm](https://www.npmjs.com/package/skills)

## Catálogo navegável

Espelho do repositório gerado diretamente dos `SKILL.md`, com cada skill, grupo de engine e caminho de instalação por agente como páginas web — útil para explorar o catálogo sem clonar.

[Explore o catálogo](https://gamedev-skills.github.io/awesome-gamedev-agent-skills/)
