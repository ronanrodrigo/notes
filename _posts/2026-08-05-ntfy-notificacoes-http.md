---
title: "ntfy: Notificações push por HTTP simples"
description: "Curadoria sobre ntfy, serviço gratuito e open-source para enviar notificações push para telefone ou desktop via HTTP simples, com casos de uso, integrações e alternativas"
date: 2026-08-05
tags:
  - notificacoes
  - http
  - automacao
  - open-source
  - monitoramento
---

## ntfy: Enviar notificações push para telefone ou desktop via HTTP

ntfy (pronuncia-se "notify") é um serviço de notificação pub-sub baseado em HTTP simples e gratuito. Permite enviar notificações para seu telefone ou desktop usando requisições HTTP simples (PUT/POST) a partir de scripts, servidores, cron jobs ou agentes de IA, sem necessidade de cadastro ou pagamento.

É perfeito para:
- Scripts de longa duração
- Conclusões de agentes de IA
- Pipelines CI/CD
- Monitoramento de servidores
- Deploys e backups
- Automações em geral

[Acesse a fonte original](https://ntfy.sh/)

## Documentação e Repositório

Documentação completa com exemplos de integração, API de subscrição, headers customizados e casos de uso.

[Documentação ntfy](https://docs.ntfy.sh/)

[Repositório GitHub](https://github.com/binwiederhier/ntfy)

## Casos de Uso e Exemplos

Comunidade compartilha usos práticos: monitoramento de uptime com UptimeKuma, notificações Synology, Watchtower, TorrentBox, scripts de cron para verificação de espaço em disco, sincronização DNS, verificações ZFS, alertas de bateria (SmartHome), acompanhamento de hacks de jogos, integração com Hubitat, webhooks de monitoramento, e muito mais.

[Exemplos na documentação](https://docs.ntfy.sh/examples/)

[Como monitorar cron jobs com ntfy](https://www.michaelscheiwiller.com/blog/monitor-cronjobs-with-ntfy)

[Revolução nas notificações com ntfy: Casos de uso e melhores práticas](https://dev.to/hugovalters/revolutionizing-notifications-with-ntfysh-use-cases-benefits-and-best-practices-1gaf)

## Instalação e Deployment

Aplicativos oficiais para Android (Google Play, F-Droid) e iOS (App Store). Servidor open-source em Go, facilmente self-hostável via Docker ou apt.

[Docker Hub - ntfy](https://hub.docker.com/r/binwiederhier/ntfy)

[Como rodar ntfy no Docker](https://oneuptime.com/blog/post/2026-02-08-how-to-run-ntfy-in-docker-for-push-notifications/view)

[Medium: ntfy como serviço self-hosted](https://medium.com/@williamdonze/ntfy-self-hosted-notification-service-0f3eada6e657)

## Integrações e Automações

ntfy integra facilmente com GitHub Actions, CI/CD pipelines, ferramentas de monitoramento (Prometheus, Zabbix, Nagios), Ansible, Puppet e outras plataformas de automação.

[Automate seu workflow com ntfy](https://mbebars.medium.com/automate-your-workflow-effortless-notifications-with-ntfy-sh-ef2a71dac6b5)

## Alternativas

Competitors: Pushover, Gotify, Healthchecks.io, Home Assistant, Uptime Kuma.

[Alternativas no LibHunt](https://www.libhunt.com/r/ntfy)