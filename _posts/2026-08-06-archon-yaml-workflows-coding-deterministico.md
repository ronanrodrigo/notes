---
title: "Archon: workflows YAML para coding determinístico"
description: "Curadoria sobre o Archon, um motor de execução para agentes de IA codarem e validarem com mais previsibilidade, modelando o processo em workflows YAML."
date: 2026-08-06
tags:
  - ai-agents
  - automation
  - tools
  - design-systems
  - prompt-engineering
  - github
  - git
---

## Archon (motor de execução de agentes de IA com workflows YAML)
O Archon é apresentado como um motor de execução para agentes de coding com o objetivo de tornar o processo "determinístico e repetível". A curadoria destaca a ideia de modelar o fluxo de desenvolvimento (planejamento, implementação, validação, code review e criação de PR) em etapas rígidas via arquivos YAML.

[Acesse a fonte original](https://archon.diy/)

## Conceitos centrais: workflows em DAG com nós (AI e bash)
Explica que um workflow é definido em YAML como um grafo acíclico dirigido (DAG) com nós e dependências, misturando etapas controladas (como bash determinístico) e etapas de IA (prompt/LLM) para orquestrar as fases do trabalho.

[Acesse a fonte original](https://archon.diy/getting-started/concepts/)

## Essential Workflows: geração de YAML para o seu projeto
Mostra um caminho para criar (ou gerar) workflows YAML alinhados ao que você descreve a respeito do seu projeto, com validação do arquivo gerado e salvamento no formato esperado pelo Archon.

[Acesse a fonte original](https://archon.diy/book/essential-workflows/)

## Repositório oficial: coleam00/Archon
Documento principal do projeto com posicionamento (harness builder), instalação e referências para começar a usar o Archon.

[Acesse a fonte original](https://github.com/coleam00/Archon)
