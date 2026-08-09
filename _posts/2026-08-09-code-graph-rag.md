---
title: "Code-Graph-RAG: Transformando Repositórios em Grafos de Conhecimento"
description: "Sistema RAG baseado em grafos que transforma repositórios em grafos de conhecimento usando Tree-sitter, Memgraph e LLMs para análise e compreensão de codebases."
date: 2026-08-09
tags:
  - rag
  - ai-agents
  - tools
  - design-systems
  - local-llm
  - mobile
  - github
---

## Code-Graph-RAG: Sistema RAG Baseado em Grafos para Análise de Codebases

Em vez de tratar um repositório apenas como texto, o Code-Graph-RAG transforma o código em um grafo de conhecimento, preservando a estrutura e os relacionamentos entre arquivos, classes, funções e módulos.

Isso significa que um agente pode entender melhor como o sistema está organizado, navegando por dependências reais em vez de depender apenas da similaridade entre trechos de código.

[Acesse o repositório no GitHub](https://github.com/vitali87/code-graph-rag)

## Arquitetura e Componentes Principais

O projeto combina tecnologias complementares:

- **Tree-sitter**: Análise robusta e agnóstica de linguagem usando Abstract Syntax Trees (AST)
- **Memgraph**: Armazenamento de grafos de conhecimento com suporte a consultas estruturadas via Cypher
- **LLMs**: Integração com Google Gemini, OpenAI e Ollama para traduzir perguntas em linguagem natural para queries no grafo
- **AST-based Code Editing**: Edição cirúrgica de código com substituição precisa baseada em AST

O sistema opera em duas etapas principais: parsing e ingestion (extração de estrutura do código para o grafo) e query (consultas interativas em linguagem natural contra o grafo).

## Capacidades e Funcionalidades

O Code-Graph-RAG oferece várias operações:

- **Consultas em Linguagem Natural**: Pergunte sobre a estrutura e relações do código em português ou inglês
- **Busca Semântica**: Recuperação de funções baseada em embeddings vetoriais e propósito
- **Edição Cirúrgica de Código**: Substituição AST-based com visualização de diffs
- **Otimização com IA**: Sugestões de otimização com aprovação interativa
- **Análise de Dependências**: Mapeamento de call graphs e detecção de código morto
- **Integração MCP**: Funciona como servidor Model Context Protocol para Claude Code e outros clientes
- **Multi-linguagem**: Suporte a 12+ linguagens incluindo Python, TypeScript, Rust, Go, Java, C, C++, PHP, Scala e C#

## Casos de Uso Ideais

O sistema é especialmente útil para:

- **Grandes codebases**: Compreender arquitetura e relacionamentos em projetos grandes
- **Monorepos**: Navegar entre múltiplos pacotes e módulos interdependentes
- **Manutenção de Sistemas Legados**: Entender estrutura e dependências de código antigo
- **Agentes de IA para Engenharia de Software**: Fornecer contexto estruturado para agentes que precisam entender e editar código
- **Análise de Impacto**: Determinar quais arquivos são afetados por mudanças em pontos críticos

## Instalação e Uso Rápido

```bash
# Instalação via uv (recomendado) ou pipx
uv tool install "code-graph-rag[treesitter-full,semantic]"

# Iniciar a CLI interativa
python -m codebase_rag.main start --repo-path /path/to/your/repo --update-graph

# Ou usar como servidor MCP
code-graph-rag mcp-server
```

Os requisitos do sistema incluem Docker (para Memgraph), cmake e ripgrep, conforme documentado no repositório.

## Pesquisa Acadêmica e Validação

Estudos comparativos demonstram a eficácia de grafos baseados em AST em relação a grafos extraídos por LLMs:

- **Grafos AST-Derived vs LLM-Extracted**: Pesquisa mostra que grafos determinísticos baseados em Tree-sitter oferecem cobertura mais confiável, latência menor, menores custos de indexação e maior precisão em multi-hop queries comparados a grafos gerados por LLMs
- **RAG para Conclusão de Código**: Estudos demonstram que abordagens híbridas combinando busca lexical (BM25) e semântica alcançam melhor performance em conclusão de código

## Recursos Adicionais

- **Documentação Oficial**: https://docs.code-graph-rag.com/
- **PyPI**: https://pypi.org/project/code-graph-rag/
- **Site Principal**: https://code-graph-rag.com/
- **MCP App Store**: https://mcpapp-store.com/apps/code-graph-rag

## Perspectivas Futuras

O Code-Graph-RAG representa uma mudança promissora na forma como agentes de IA trabalham com código. Em vez de buscar fragmentos de texto similares, os agentes podem navegar pela arquitetura real do projeto, compreender dependências complexas e executar edições precisas — um avanço significativo para automação de engenharia de software.
