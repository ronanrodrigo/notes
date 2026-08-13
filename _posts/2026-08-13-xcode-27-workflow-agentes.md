---
title: "Xcode 27: um fluxo de trabalho para agentes de programação"
description: "Uma curadoria sobre o uso de planejamento, mudanças delimitadas, revisão, testes e análise de perfil ao trabalhar com agentes no Xcode 27."
date: 2026-08-13
tags:
  - ai-agents
  - desenvolvimento
  - swift
layout: post
---

## Fluxo de trabalho para Xcode 27 compartilhado em imagem

A imagem compartilhada propõe usar agentes de programação com escopo e supervisão: definir o plano e as restrições, executar uma mudança focada, revisar os diffs relevantes, rodar testes, consultar ferramentas de perfil quando fizer sentido e manter a responsabilidade humana pela arquitetura, segurança e aprovação antes do merge. Como a imagem não informa uma fonte pública, este item é descrito somente a partir do conteúdo visual recebido.

## O que há de novo no Xcode 27

Na apresentação da Apple, o Xcode 27 mostra agentes trabalhando no editor, com modo de planejamento para explorar e alinhar a arquitetura antes da implementação. O material também relaciona o fluxo a previews, builds e testes para verificar o resultado.

[Assista a “What’s new in Xcode 27”](https://developer.apple.com/videos/play/wwdc2026/258/)

## Planejamento e revisão antes de alterar o código

A documentação de release do Xcode 27 descreve planos como artefatos Markdown editáveis ao lado da conversa, com possibilidade de revisão, anotações e aprovação antes de o agente prosseguir. Ela também apresenta diffs e outros artefatos gerados pelo agente no mesmo contexto de trabalho.

[Leia as notas de release do Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)

## Controle de ferramentas e permissões dos agentes

As configurações de Coding Intelligence permitem controlar comandos, ferramentas e skills que um agente pode usar. A documentação também esclarece que agentes podem acessar informações do projeto ao processar pedidos, tornando a definição de escopo e a revisão humana partes importantes do fluxo.

[Consulte a documentação de Coding Intelligence](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence)
