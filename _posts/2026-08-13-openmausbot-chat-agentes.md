---
title: "OpenMausBot: um chat desktop para uma equipe de agentes"
description: "Um app open source, local-first, que organiza Claude, Codex e outros agentes como contatos em uma interface de conversa."
date: 2026-08-13
tags:
  - ai-agents
  - agentes
  - open-source
  - mcp
  - claude
  - codex
layout: post
---

## OpenMausBot

O OpenMausBot transforma uma equipe de agentes em uma interface de chat: cada bot pode ter sua própria personalidade, modelo, memória de thread, computador e aplicativos conectados. O projeto é local-first, usa as CLIs instaladas de Claude, Codex ou Grok e concentra os processos em um harness local com eventos transmitidos por SSE.

O destaque é a combinação entre conversação e execução observável: comandos de shell, edições de arquivos e perguntas aparecem como pedidos de permissão; cada bot também pode usar um computador na nuvem ou o próprio Mac. A integração com Composio Connect adiciona Gmail, Slack, GitHub, Notion, Linear e centenas de outros aplicativos.

[Acesse o repositório do OpenMausBot](https://github.com/milind-soni/OpenMausBot/tree/main)

## Claude Code: a CLI por trás de um dos agentes

Para entender o tipo de agente que o OpenMausBot pode orquestrar, vale consultar a documentação oficial do Claude Code. Ela explica como a ferramenta explora o contexto do projeto, edita arquivos, executa comandos, trabalha com Git e integra fontes externas por MCP — exatamente o modelo de agente que ganha uma camada de interface e coordenação no OpenMausBot.

[Leia a documentação oficial do Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started)

