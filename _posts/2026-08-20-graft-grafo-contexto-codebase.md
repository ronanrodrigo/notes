---
title: "Graft: contexto persistente para agentes de programação"
description: "Curadoria sobre uma ferramenta open-source que transforma repositórios em grafos de contexto legíveis por agentes de código."
date: 2026-08-20
tags:
  - ai-agents
  - code-analysis
  - open-source
  - mcp
  - tree-sitter
layout: post
---

## Graft

Ferramenta open-source que constrói um grafo de contexto do repositório em arquivos Markdown ligados entre si. O projeto combina cartões estruturais determinísticos, análise com Tree-sitter e uma etapa opcional com LLM para produzir resumos, trechos centrais, fontes e relações entre subsistemas. A CLI também oferece orientação do repositório, busca por regex, análise de callers, skeletons e integração com agentes como Claude Code, Cursor, Codex e Gemini.

[Acesse o projeto no GitHub](https://github.com/NanoNets/Graft)

## Benchmark: Cold Claude Code vs. Claude Code + Graft

Benchmark controlado de 162 execuções (mesmo agente, mesmas ferramentas de arquivo, mudando só o contexto): 46% menos tool calls, 42% menos tokens e 60% menos tempo, sem perda de corretude. Os picos por tarefa chegam a 4x mais barato e 3x mais rápido. A metodologia inclui reprodução dos cinco PRs merged do SWE-bench avaliado com 21% menos custo.

[Acesse a fonte original](https://github.com/NanoNets/Graft)

## GitHub App: blast-radius review em todo PR

O projeto oferece um GitHub App que adiciona revisão automática de blast radius em cada pull request — mostra o que cada mudança depende e o que depende dela. Instalação direto pela página do app no repositório.

[Acesse a fonte original](https://github.com/NanoNets/Graft)

## Quick start: dois comandos

```bash
npm install -g @nanonets/graft
graft init
```

O `graft init` constrói o grafo em `graft/` (ignorado pelo git, cache local regenerável) e conecta o agente — a partir da próxima sessão, os nós correspondentes entram em cada prompt e o grafo se reconstrói em background. Funciona com Claude Code, Cursor, Codex, Gemini e qualquer agente que lê arquivos.

[Acesse a fonte original](https://graft.nanonets.ai)

## Tree-sitter

Gerador de parsers e biblioteca de parsing incremental que produz árvores sintáticas concretas e consegue atualizá-las eficientemente durante a edição. É a base técnica que torna possível ao Graft construir seu grafo estrutural sem depender de um modelo ou de uma rede.

[Leia a introdução oficial ao Tree-sitter](https://tree-sitter.github.io/tree-sitter/)

## Model Context Protocol

Especificação do protocolo que padroniza como aplicações de LLM descobrem e invocam ferramentas oferecidas por servidores. O Graft expõe um servidor MCP para disponibilizar consultas de contexto do código aos agentes que suportam esse padrão.

[Consulte a especificação oficial do MCP](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
