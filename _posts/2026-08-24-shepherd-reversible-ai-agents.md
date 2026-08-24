---
title: "Shepherd: Execução Reversível para Agentes de IA"
description: "Framework Python para traços de execução reversíveis, permitindo que meta-agentes observem, bifurquem, reproduzam e revertam execuções de agentes."
date: 2026-08-24
tags:
  - agents
  - ai
  - python
  - security
  - automation
---

## Shepherd

Framework em alpha inicial que transforma a execução de agentes em um traço reversível estilo Git. Registra saídas como traços duráveis para revisão antes da aplicação, com enforcement de permissões em nível de syscall (macOS Seatbelt e Linux Landlock). Requer Python 3.11+ e não suporta Windows.

[Acesse a fonte original](https://github.com/shepherd-agents/shepherd)

## Shepherd: Enabling Programmable Meta-Agents via Reversible Agentic Execution Traces

Artigo no arXiv apresentando Shepherd como substrate Python baseado em princípios de programação funcional, onde a execução do agente é um objeto de primeira classe que meta-agentes podem inspecionar e transformar. Cada ação do modelo, chamada de ferramenta e mudança de ambiente vira um evento estruturado em um traço de execução reversível.

[Acesse a fonte original](https://arxiv.org/abs/2605.10913)

## Shepherd: runtime substrate for reversible agentic execution

Descrição do projeto destacando que Shepherd permite que meta-agentes observem, bifurquem, reproduzam e revertam qualquer execução de agente. Acopla agente e ambiente em um fork copy-on-write aproximadamente 5x mais rápido que docker commit, com cerca de 95% de reutilização de KV cache.

[Acesse a fonte original](https://github.com/shepherd-agents/shepherd)

## Shepherd Python Meta-Agent Framework

Framework open-source que permite fork, replay e revert de execuções de agentes. Projetado para meta-agentes que supervisionam, otimizam e treinam outros agentes, com sistema de permissões definido nas assinaturas das funções.

[Acesse a fonte original](https://dailytech.ai/post/shepherd-python-meta-agent-framework-fork-replay-revert/)

## Shepherd | AI Native Landscape

Visão geral do projeto enfatizando traços de execução reversíveis estilo Git, fork copy-on-write e suporte para tree-search e otimização estilo RL sobre trajetórias de agentes.

[Acesse a fonte original](https://landscape.jimmysong.io/projects/shepherd/)
