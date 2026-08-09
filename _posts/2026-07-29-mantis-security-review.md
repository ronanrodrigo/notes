---
title: Mantis — Agentes de IA para Revisão de Segurança em Software
date: 2026-07-29
tags:
  - security
  - ai-agents
  - code-review
layout: post
description: 'Como agentes especializados podem analisar, reproduzir e corrigir vulnerabilidades de software.'
---

## Mantis: Toolkit para Revisão de Segurança

Recentemente descobri Mantis, um projeto open-source do Google que muda fundamentalmente como pensamos sobre segurança em software com IA. Diferente de muitos frameworks para agentes, o foco não é criar chatbots ou automatizar tarefas genéricas.

O objetivo é outro: transformar agentes de IA em **revisores de segurança de software**.

O Mantis fornece um conjunto modular de skills para que agentes consigam:

- Analisar arquiteturas de software
- Identificar vulnerabilidades
- Reproduzir os problemas encontrados
- Propor ou até gerar correções automaticamente

Um ponto interessante é que ele é **stack-agnóstico**, ou seja, não depende de uma linguagem, framework ou plataforma específica. A ideia é que as habilidades possam ser reutilizadas em diferentes ambientes e agentes de IA.

Esse tipo de projeto mostra uma tendência importante: estamos entrando na era em que agentes executam fluxos especializados, combinando conhecimento, planejamento e ferramentas para resolver problemas complexos.

Para quem trabalha com IA aplicada, DevSecOps ou engenharia de software, vale a pena acompanhar.

**Observação:** O projeto ainda é experimental e não é recomendado para uso em produção. A proposta é servir como uma base para pesquisa, experimentação e evolução de agentes especializados em segurança de software.

[Repositório oficial no GitHub](https://github.com/google/mantis)

---

## Arquitetura e Pipeline do Mantis

O Mantis Skills é um toolkit decentralizado, sequencial e focado em segurança. A documentação oficial descreve uma arquitetura de 15 estágios coordenados por um agente supervisor (`mantis_meta_agent`):

1. **Strategist Agent** — Avalia a estrutura geral do código, modelos de ameaça e grafos de dependência para isolar padrões de risco arquitetural
2. **Research Agents** — Agentes especializados que investigam arquivos brutos, examinando fluxos de dados e lógica de sanitização
3. **Deduplicator, Reviewer e Critic Agents** — Filtram ruído e eliminam falsos positivos
4. **Reproduction Sandbox** — Executa provas de conceito geradas automaticamente em ambiente isolado e emulado

Os resultados são arquivados com histórico de aprendizado (`learnings.jsonl`), permitindo que o sistema se adapte across iterative runs e evite análises redundantes.

A redução de tokens é significativa: ao condensar arquivos individuais em sumários hierárquicos de diretório e raiz, o Mantis reduz overhead de tokens em mais de 85% mantendo contexto estrutural crítico em repositórios grandes.

[Documentação completa e especificação técnica](https://github.com/google/mantis)

---

## Segurança em Agentes de IA: Contexto de 2026

Em 2026, agentes de IA enfrentam riscos de segurança bem específicos. O panorama mudou significativamente:

**Principais vulnerabilidades em agentes agentic:**
- **Prompt injection** — Hackers injetam instruções maliciosas que desviam a lógica do agente
- **Memory poisoning** — Corrupção de memória de longo prazo do agente com comportamentos prejudiciais
- **Tool abuse** — Exploração de APIs e integrações para ações não autorizadas ou DDoS
- **Data leakage** — Exposição de dados sensíveis em logs ou sistemas externos
- **Supply chain attacks** — Compromisso de plugins, skills ou dependências terceirizadas
- **Privilege compromise** — Concessão excessiva de permissões exploradas por agentes enganados

Segundo o OWASP Top 10 for Agentic Applications 2026 (lançado em dezembro de 2025), a maioria dos incidentes de 2026 envolveu o Model Context Protocol (MCP) como vetor de ataque — arquivos de configuração envenenados, skills maliciosas e servidores MCP expostos sem autenticação.

[OWASP Top 10 Agentic Applications 2026](https://owasp.org/)

---

## GitHub Copilot CLI: Security Review (Experimental)

Em junho de 2026, GitHub lançou um comando experimental `/security-review` no Copilot CLI. É uma alternativa mais leve ao Mantis, focada em mudanças de código em tempo de desenvolvimento.

O comando analisa alterações locais e retorna:
- Descobertas de segurança com confiança e severidade
- Sugestões acionáveis direto no terminal
- Foco em 11 categorias de vulnerabilidades: injection flaws, XSS, broken access control, path traversal, SSRF, insecure deserialization, weak cryptography, hardcoded credentials, sensitive data leaks, authentication/CORS failures, e supply-chain risks

Diferente do Mantis (que é agentic e orquestrado), o Copilot CLI `/security-review` é um atalho rápido para perguntar "introduzi um problema de segurança?" antes de um pull request.

[GitHub Blog: Dedicated security review command](https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli/)

---

## Ferramentas e Frameworks Relacionados

A paisagem de segurança com IA em 2026 inclui diversas abordagens:

**Agentic security reviewers:**
- OpenAI Codex Security
- Checkmarx Developer Assist
- Claude-based semantic SAST (Anthropic)

**Platform-native scanners:**
- GitHub Advanced Security
- Snyk Code
- Semgrep

**Supply chain e reachability:**
- Endor Labs AURI
- Socket

Cada ferramenta usa machine learning ou LLMs para encontrar vulnerabilidades, sugerir fixings validados e integrar-se com agentes de codificação via Model Context Protocol.

[7 AI Application-Security Tools for 2026](https://securityboulevard.com/2026/06/7-ai-application-security-tools-for-2026/)

---

## Conclusão

Mantis representa um step importante em como defesa de segurança e IA se encontram. Enquanto agentes de codificação já são realidade, ter agentes especializados em **encontrar** e **validar** vulnerabilidades muda o jogo na hora que a maioria dos codigos gerados por IA ainda era encarado com desconfiança.

A modularidade e a reutilização de skills em diferentes ambientes apontam para um futuro onde segurança é um layer integrado desde o planejamento até a reprodução de exploits.

Para times interessados em DevSecOps moderno, pesquisa em agentes de IA ou vulnerability research, acompanhar Mantis é recomendado — não necessariamente em produção hoje, mas como indicador de tendência e ferramenta de experimentação.
