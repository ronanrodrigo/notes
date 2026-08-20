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

## Tree-sitter

Gerador de parsers e biblioteca de parsing incremental que produz árvores sintáticas concretas e consegue atualizá-las eficientemente durante a edição. É a base técnica que torna possível ao Graft construir seu grafo estrutural sem depender de um modelo ou de uma rede.

[Leia a introdução oficial ao Tree-sitter](https://tree-sitter.github.io/tree-sitter/)

## Model Context Protocol

Especificação do protocolo que padroniza como aplicações de LLM descobrem e invocam ferramentas oferecidas por servidores. O Graft expõe um servidor MCP para disponibilizar consultas de contexto do código aos agentes que suportam esse padrão.

[Consulte a especificação oficial do MCP](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
