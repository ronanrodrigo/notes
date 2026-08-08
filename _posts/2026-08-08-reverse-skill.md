---
title: "Reverse-Skill: Roteador de Skills para Engenharia Reversa com IA"
description: "Framework open-source que integra agentes de IA para engenharia reversa com matriz de roteamento estruturada e fluxos de segurança automatizados"
date: 2026-08-08
tags:
  - reverse-engineering
  - ai-agents
  - cybersecurity
  - pentesting
  - malware-analysis
  - ctf
---

## Reverse-Skill: Framework de Engenharia Reversa com IA

Um framework open-source que funciona como roteador de skills para agentes de IA (Claude Code, Cursor, Cline, Windsurf) em tarefas de engenharia reversa, penetração de testes autorizados e pesquisa de segurança. Em vez de permitir que agentes adivinhem como proceder, o Reverse-Skill impõe um modelo route-first, execute-second: intercepta requisições em linguagem natural, valida contra uma matriz de roteamento mestre e direciona o agente para um contrato processual específico para essa tarefa.

Características principais:
- Roteamento AI-driven para fluxos de segurança (APK, binários, JavaScript, malware, CTF, firmware)
- Matriz de roteamento mestre e playbooks estruturados
- Bootstrap de dependências com verificação SHA256
- Portão de autorização antes de tocar em um alvo
- Integração com Ghidra, IDA Pro, Radare2, Frida, Burp Suite e mais
- Módulo MCP (Model Context Protocol) para integração com agentes
- Field-journal logging para rastreamento de execução

[Acesse o repositório no GitHub](https://github.com/zhaoxuya520/reverse-skill)

## Ferramentas Complementares para APK e Análise Dinâmica

**JADX** - Decompilador open-source que converte bytecode DEX dentro de APKs em código Java legível, facilitando a análise estática sem acesso ao código-fonte original.

[Saiba mais sobre JADX](https://blog.ostorlab.co/top-10-mobile-pentesting-tools-in-2026.html)

**Ghidra** - Framework de engenharia reversa open-source desenvolvido pela NSA para suportar análise binária profunda e pesquisa de vulnerabilidades em múltiplas plataformas.

[Saiba mais sobre Ghidra](https://blog.ostorlab.co/top-10-mobile-pentesting-tools-in-2026.html)

**Frida** - Toolkit de instrumentação dinâmica que permite injetar scripts em aplicações em execução para debugging, engenharia reversa, testes de segurança e bypass de controles.

[Saiba mais sobre Frida](https://www.globalapptesting.com/blog/android-app-penetration-testing-tools)

**Mobile Security Framework (MobSF)** - Plataforma open-source para testes de segurança de aplicações móveis (Android, iOS, Windows). Oferece análise estática e dinâmica integrada com detecção de vulnerabilidades e monitoramento em tempo de execução.

[Saiba mais sobre MobSF](https://medevel.com/android-pentesting-tools-22/)

## Metodologia Prática de APK Pentesting

Workflow recomendado para análise de aplicativos Android:
1. Extração: usar `adb pull` ou cópia direto da Play Store
2. Análise Estática: decompilação com apktool + jadx para código legível
3. Inspeção: revisar AndroidManifest.xml para componentes exportados e permissões perigosas
4. Busca de Secrets: procurar hardcoded secrets, chaves API e endpoints
5. Análise Dinâmica: deploy de frida-server, bypass de SSL pinning com objection
6. Interceptação: usar Burp Suite para captura de tráfego criptografado

[Acesse o guia completo de Android Pentesting](https://payloadplayground.com/blog/android-penetration-testing-guide)

## Repositórios Relacionados de Segurança Mobile

**android-security-awesome** - Curadoria abrangente de ferramentas, recursos e frameworks para segurança Android, incluindo analisadores online, decompiladores e frameworks de análise dinâmica.

[Explore android-security-awesome](https://github.com/ashishb/android-security-awesome)

**APKDeepLens** - Ferramenta em Python para escanear APKs em busca de vulnerabilidades alinhadas ao OWASP Top 10 mobile, útil para desenvolvedores e pesquisadores de segurança.

[Explore APKDeepLens](https://github.com/d78ui98/APKDeepLens)