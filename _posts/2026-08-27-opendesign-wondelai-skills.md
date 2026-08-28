---
title: "OpenDesign e Wondel.ai: design generativo e skills de negócio para agentes"
description: "Dois repositórios que estendem agentes de código — um app desktop open-source de design e uma coleção de skills baseadas em livros best-sellers — ambos sobre o padrão Agent Skills."
date: 2026-08-27
tags:
  - agent-skills
  - ai-agents
  - open-source
  - claude
  - design-systems
  - tools
layout: post
---

## OpenDesign: alternativa open-source ao Claude Design

App desktop local-first para macOS e Windows que transforma seu agente de código em motor de design. Gera protótipos web, desktop e mobile, dashboards, decks, imagens e vídeo, com exportação para HTML, PDF, PPTX e MP4 e preview em iframe sandboxed. Roda sobre DeepSeek Harness (dsh), Claude Code, Codex, Cursor, OpenCode e mais de 20 CLIs via BYOK, e adota o padrão de skills `SKILL.md` da Anthropic. Licença Apache-2.0; site em open-design.ai.

[Acesse o repositório](https://github.com/nexu-io/open-design)

## Wondel.ai Agent Skills

Coleção de mais de 50 skills e 12 jornadas guiadas que destilam frameworks de livros best-sellers de negócios, marketing, UX e engenharia — StoryBrand, Made to Stick, Blue Ocean Strategy, Clean Code, Domain-Driven Design e outros. Instala via marketplace de plugins do Claude Code, `npx skills add` (skills.sh), plugins do Codex e Agent Plugins (agent-plugins.org). As metaskills orquestram as skills em fluxos de create/improve/grow para negócio, site e app. Licença MIT; catálogo em skills.wondel.ai.

[Acesse o repositório](https://github.com/wondelai/skills)

## Skills da Anthropic (repositório oficial)

Repositório público com skills de exemplo da Anthropic para Claude — criativas, técnicas e corporativas — e o local que abriga a especificação e o template oficial do formato Agent Skills. É a referência canônica do padrão `SKILL.md` adotado por ferramentas como OpenDesign e Wondel.ai.

[Acesse o repositório oficial](https://github.com/anthropics/skills)

## Agent Skills: o padrão aberto

Formato leve e aberto para estender capacidades de agentes com conhecimento e fluxos especializados. No núcleo está uma pasta com `SKILL.md` (metadados `name`/`description` + instruções), com carregamento progressivo em três estágios: descoberta, ativação e execução. Originalmente desenvolvido pela Anthropic e liberado como padrão aberto, com adoção crescente por diversos clientes de agentes.

[Leia a especificação](https://agentskills.io)
