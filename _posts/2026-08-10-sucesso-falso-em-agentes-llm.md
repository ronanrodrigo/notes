---
title: "Sucesso falso em agentes LLM: do fechamento confiante à falha silenciosa"
description: "Curadoria sobre o paper que mede quando agentes de LLM afirmam concluir tarefas mesmo com estado do ambiente indicando falha, e discute detectores leves como TF-IDF."
date: 2026-08-10
tags:
  - ai-agents
  - automation
  - code-review
---

## From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents

Paper sobre *false success* em agentes LLM: o agente encerra com uma mensagem de conclusão/sucesso enquanto o estado do ambiente indica que a ação não ocorreu. Os autores analisam trajetórias em dois benchmarks de agentes e mostram que juízes baseados em LLM têm desempenho limitado para esse tipo de falha, enquanto detectores leves (por exemplo, TF-IDF) conseguem sinalizar false success com boa precisão/recall e baixa latência. [Acesse a fonte original](https://arxiv.org/abs/2606.09863)

## When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

Complemento sobre falhas silenciosas em runtime de agente em produção: propõe uma taxonomia de como erros podem ser “diluídos”, não chegarem como sinal acionável e, em alguns casos, serem convertidos em narrativas coerentes (plausíveis, mas erradas) para o usuário. [Acesse a fonte original](https://arxiv.org/abs/2606.14589)
