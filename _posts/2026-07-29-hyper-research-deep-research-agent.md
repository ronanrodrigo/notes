---
title: Hyper Research - agente de pesquisa profunda com pipeline adaptativo
date: 2026-07-29
tags:
  - ai-agents
  - claude
  - open-sourcedescription: 'Um pipeline open source para pesquisa profunda com verificação, proveniência e memória persistente.'
---

## Hyper Research

Projeto open-source que transforma Claude Code em um agente de pesquisa profunda. Implementa um pipeline adaptativo de 16 passos que produz relatórios auditados adversarialmente com proveniência completa de fontes. Lidera o leaderboard DeepResearch-Bench RACE internamente.

Características principais:
- **Pipeline tier-adaptive de 16 passos**: processa um prompt e gera um relatório com verificação completa
- **Vault persistente e pesquisável**: cada fonte lida é armazenada em SQLite, compondo conhecimento entre sessões
- **Verificação de fatos adversarial**: auditoria integrada para garantir precisão
- **Markdown como verdade, SQLite como cache**: notas com YAML frontmatter em `research/notes/`

[Acesse o repositório no GitHub](https://github.com/jordan-gibbs/hyperresearch)

## DeepResearch-Bench: avaliação de agentes de pesquisa

Benchmark com 100 tarefas em nível PhD (22 domínios, 50 em inglês + 50 em chinês) para avaliar agentes de pesquisa profunda. Propõe dois frameworks de avaliação:

- **RACE** (Reference-based Adaptive Criteria-driven Evaluation): avalia qualidade de relatórios em 4 dimensões dinâmicas — abrangência, profundidade, seguimento de instruções, legibilidade
- **FACT** (Framework for Factual Abundance and Citation Trustworthiness): verifica se as fontes citadas realmente suportam as afirmações

Resultados mostram que Gemini-2.5-Pro Deep Research lidera (48,88 no RACE), seguido de OpenAI Deep Research (46,98). Validação humana confirma 71,33% de concordância com avaliadores especialistas.

[Acesse o benchmark e leaderboard](https://deepresearch-bench.github.io/)

## Crawl4AI: web crawler otimizado para LLMs

Biblioteca open-source Python para web crawling e extração de dados, otimizada para LLMs e agentes de IA. Usado pelo Hyper Research para coletar informações mais amplas que ferramentas de busca padrão. Suporta sessões autenticadas para LinkedIn e Twitter.

[Acesse a documentação](https://docs.crawl4ai.com/)

## Arquitetura de agentes de pesquisa profunda

A categoria emergente de agentes de pesquisa profunda (Deep Research Agents) combina:
- Raciocínio dinâmico e planejamento adaptativo de longo horizonte
- Recuperação multi-hop de informações
- Uso iterativo de ferramentas
- Geração de relatórios estruturados com análise

Diferentes modelos (Claude, Gemini, GPT-4o) excelem em dimensões distintas — OpenAI destaca-se em seguimento de instruções, enquanto Gemini lida melhor com abrangência e citações efetivas.

[Leia o artigo: Deep Research Agents: A Systematic Examination](https://arxiv.org/html/2506.18096v2)

## Memória persistente em Claude Code

Mecanismos para manter conhecimento entre sessões:
- **CLAUDE.md**: instruções persistentes que guiam comportamento do agente
- **Auto memory**: Claude escreve notas sobre aprendizados, correções e padrões
- **Agent Memory**: armazenamento persistente para subagentes (v2.1.33+)
- **Tasks on-disk**: tarefas como grafo de dependência (v2.1.16+)

Permite que agentes acumulem conhecimento e melhorem com o tempo — exatamente o que Hyper Research implementa com seu vault SQLite.

[Acesse a documentação de memória do Claude Code](https://code.claude.com/docs/en/memory)