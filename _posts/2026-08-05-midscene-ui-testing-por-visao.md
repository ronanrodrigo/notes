---
title: "Midscene: UI testing por visão"
description: "Curadoria sobre o Midscene.js, SDK open-source para automação visual de interfaces com linguagem natural, Playwright, mobile e desktop."
date: 2026-08-05
tags:
  - testing
  - automation
  - open-sourcelayout: post
---

## Print compartilhado pelo usuário

O print destaca o Midscene.js como um SDK open-source de UI testing guiado por visão, com testes em linguagem natural, menor dependência do DOM e foco em automação cross-platform. A imagem também enfatiza o uso em navegador, iOS e outros ambientes, além da ideia de automatizar fluxos reais sem IDs estáticos.

## O que é o Midscene.js

Midscene é um SDK open-source de automação visual para UI testing. A documentação oficial descreve suporte a web, Android, iOS, HarmonyOS, desktop e canvas, com dois modos de uso principais: planejamento autônomo de tarefas e fluxo orientado por passos.

[Acesse a fonte original](https://midscenejs.com/introduction)

## Repositório oficial

O repositório principal concentra o código, exemplos e a visão geral do projeto. O README destaca integração com Playwright e Puppeteer, uso com Android e o apoio a modelos multimodais voltados para localização visual.

[Acesse a fonte original](https://github.com/web-infra-dev/midscene)

## Como ele entra em projetos reais

O projeto se integra com Playwright e Puppeteer para testes web, com Android via adb e iOS via WebDriverAgent. Também existe o caminho de Skills, para que agentes de IA controlem browser, desktop e dispositivos móveis por linha de comando.

[Acesse a fonte original](https://midscenejs.com/skills)
[Acesse a fonte original](https://midscenejs.com/integrate-with-playwright)

## Modelos e estratégia

A documentação de model strategy explica que o Midscene depende de modelos multimodais com boa capacidade de grounding visual. Há suporte a combinação de modelos, inclusive opções open source, para melhorar localização de elementos e desempenho em cenários diferentes.

[Acesse a fonte original](https://midscenejs.com/model-strategy)

## Evolução recente

O changelog mostra que o projeto vem evoluindo rápido: scripts em estilo BDD, refinamentos em cache e planejamento, além da migração do uso de MCP para Skills e CLIs como caminho recomendado para agentes.

[Acesse a fonte original](https://midscenejs.com/changelog)

## Exemplos e documentação complementar

O repositório de exemplos ajuda a entender as integrações com Playwright, Puppeteer, Android e YAML. O pacote `@midscene/web` também mostra o ponto de entrada do SDK para automação visual no ecossistema npm.

[Acesse a fonte original](https://github.com/web-infra-dev/midscene-example)
[Acesse a fonte original](https://www.npmjs.com/package/@midscene/web)
