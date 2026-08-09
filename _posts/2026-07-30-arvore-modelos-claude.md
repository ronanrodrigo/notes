---
title: Árvore de Modelos do Claude
date: 2026-07-30
tags:
  - claude
  - llm
  - model-routing
  - prompt-engineering
layout: post
description: 'Guia visual para escolher entre modelos Claude conforme velocidade, complexidade e custo.'
---

## Árvore de Modelos do Claude

Imagem que apresenta um fluxograma decisório para escolher entre **Haiku 4.5**, **Sonnet 5**, **Opus 4.8** e **Fable 5**. A árvore começa com a pergunta "A sua tarefa exige mais do que uma resposta rápida?" e ramifica-se em dois caminhos que exploram critérios como necessidade de velocidade/tokens, complexidade da tarefa e ambição do objetivo. Inclui características de cada modelo (velocidade, tokens econômicos/máximos, exemplos de prompts, conectores e ferramentas suportadas).

[Acesse a fonte original](https://claude.com/resources/tutorials/choosing-the-right-claude-model)

## Escolhendo o modelo certo — Guia oficial da Claude

Documento interativo que explica o propósito e as vantagens de cada modelo:

- **Haiku 4.5**: rápido e leve, para respostas instantâneas e simples consultas.
- **Sonnet 5**: o "daily driver", para codificação, escrita, análise e resolução de problemas do dia a dia.
- **Opus 4.8**: especialista em raciocínio profundo, para tarefas complexas que exigem análise prolongada.
- **Fable 5**: para tarefas longas e complexas, com trabalho autônomo e raciocínio avançado.

Inclui exemplos de quando usar cada modelo e como selecioná-lo na interface do Claude.

[Acesse a fonte original](https://claude.com/resources/tutorials/choosing-the-right-claude-model)

## Visão geral dos modelos — Claude Platform Docs

Referência oficial de características de cada modelo: contexto, saída máxima, preço por milhão de tokens, latência, suporte a extended thinking, adaptive thinking, data de corte de conhecimento.

Organizada em tabela comparativa para rápida consulta e decisão técnica.

[Acesse a fonte original](https://platform.claude.com/docs/pt-BR/about-claude/models/overview)

## Fatores de seleção de modelo (capabilities, speed, cost, effort)

Guia que orienta como considerar requisitos reais ao decidir qual modelo usar:

- Capacidades necessárias (raciocínio, codificação, análise).
- Velocidade esperada (latência, tempo de resposta).
- Custo (por milhão de tokens, volume esperado).
- Esforço (tradeoff entre inteligência e latência/custo dentro de um único modelo).

Inclui matriz de decisão e exemplos de casos de uso.

[Acesse a fonte original](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)

## Configuração de modelos no Claude Code (aliases e seleção)

Documentação sobre como selecionar Haiku, Sonnet, Opus ou Fable no ecossistema Claude Code:

- Aliases disponíveis (`/model haiku`, `/model sonnet`, etc.).
- Como alternar modelos durante uma sessão.
- IDs de modelo para API (ex.: `claude-haiku-4-5-20251001`).
- Configuração padrão por projeto.

[Acesse a fonte original](https://code.claude.com/docs/en/model-config)

## Ativando e usando busca na web no Claude

Help Center Anthropic sobre como habilitar a feature "web search" nos modelos:

- Quais modelos suportam web search (Haiku 4.5, Sonnet, Opus, Fable).
- Como ativar no nível de workspace/organização.
- Como habilitar por conversa individual.
- Usar via prompt ("Pesquise a web") ou toggle na interface.

[Acesse a fonte original](https://support.claude.com/pt/articles/10684626-ativando-e-usando-busca-na-web)