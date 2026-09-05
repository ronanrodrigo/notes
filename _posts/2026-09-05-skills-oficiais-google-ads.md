---
title: "Skills oficiais do Google Ads para agentes de IA"
description: "Google liberou pacote gratuito de agent skills para Ads, Analytics, Gemini, Cloud e Firebase, além do MCP server oficial do Google Ads."
date: 2026-09-05
tags:
  - agent-skills
  - ai-agents
  - mcp
  - tools
  - open-source
layout: post
---

## Carrossel do Hudson Brendon sobre as skills do Google

Sequência de posts de Hudson Brendon (@99hud) mostrando que o Google liberou de graça um pacote de agent skills: são 132 manuais prontos, um para cada ferramenta — Ads, Analytics, Gemini, Cloud e Firebase. Só de Google Ads são 13 skills, escritas por quem fez a ferramenta. Uma delas diagnostica a conta sozinha — queda de conversão, verba travada, anúncio perdendo impressão. Há também o MCP oficial do Google Ads: conecta o Claude na conta e pergunta em português. A mensagem central é que essas skills não fazem o trabalho no lugar do gestor, mas tiram o braçal de ler documentação e cavar relatório do caminho.

## Agent Skills for Google products and technologies

Repositório oficial do Google com skills para agentes de IA cobrindo Ads, Analytics, Gemini, Cloud, Firebase, BigQuery, GKE e Agent Platform. Cada skill é um manual estruturado que orienta o agente no uso da ferramenta correspondente.

[Acesse a fonte original](https://github.com/google/skills)

## Google Ads MCP Server

Servidor MCP oficial e open-source (licença Apache-2.0) que conecta LLMs e agentes à Google Ads API. Expõe tools e resources para análise e consulta de dados de campanhas em linguagem natural, com autenticação via OAuth 2.0 ou service account e transporte stdio.

[Acesse a fonte original](https://github.com/googleads/google-ads-mcp)

## Google Ads MCP server: guia de integração

Documentação oficial para desenvolvedores sobre o MCP server do Google Ads: visão técnica, ciclo de interação (pergunta, descoberta de tools, execução, injeção de contexto, resposta), pré-requisitos e opções de deploy local ou no Cloud Run.

[Acesse a fonte original](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
