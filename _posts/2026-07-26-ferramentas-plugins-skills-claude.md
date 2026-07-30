---
title: "Ferramentas, Plugins e Skills do Claude"
tags: [claude, mcp, tools, integrations, skills]
date: "2026-07-26"
description: 'Visão geral de MCPs, skills, plugins e conectores para estender o Claude.'
---


Guia completo sobre as extensões e integrações do Claude: Model Context Protocol (MCP), Skills especializados e Plugins reutilizáveis.

---

## MCP Servers - Integração com Ferramentas

### Notion MCP
Leitura e escrita de páginas, bases de dados e blocos. Autenticação via OAuth ou API Key.

### Slack MCP
Ler histórico de canais, escrever mensagens, criar canvas, fazer buscas. Requer escopos específicos de permissão.

### GitHub MCP
Ler repositórios, gerenciar issues e pull requests, automatizar workflows.

### Google Workspace MCP (Community)
Integração com Sheets, Drive, Gmail, Calendar, Docs, Slides e Tasks via OAuth remoto.

### Supabase MCP
Conectar Claude a projetos Supabase com transports HTTP/SSE e OAuth.

---

## Skills - Conhecimento Especializado

Pacotes reutilizáveis que estendem o Claude com conhecimento especializado e workflows específicos da organização. Estrutura: arquivo `skill.md` com frontmatter YAML + arquivos de referência.

**Como criar:** Pasta com `skill.md` + frontmatter YAML → ZIP → Upload em Settings > Capabilities

**Como usar:** Settings > Capabilities (individual) ou Organization settings > Skills (Team/Enterprise)

---

## Plugins - Pacotes Completos

Combinam MCP Connectors, Skills, Slash Commands e Sub-agents em uma unidade compartilhável.

**Uso:** Tornar Claude especialista em um papel, time ou empresa específico.

---

## Conectores Claude Desktop

Acessar: Claude Desktop → Settings → Connectors → Add

- **Claude + Notion:** OAuth, busca, lê, cria e atualiza
- **Claude + Slack:** Requer Pro, Slack pago e aprovação do admin

---

## Recursos Úteis

- [Model Context Protocol - Documentação Oficial](https://modelcontextprotocol.io/introduction)
- [Claude Code Documentation - MCP](https://code.claude.com/docs/mcp)
- [Awesome Claude Code - Plugins & MCP Servers](https://github.com/jmanhype/awesome-claude-code)
- [Claude Skills Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Slack MCP Guide](https://slack.com/help/articles/48855576908307-Guide-to-Model-Context-Protocol-in-Slack)
- [Notion MCP Setup](https://developers.notion.com/guides/mcp/get-started-with-mcp)
