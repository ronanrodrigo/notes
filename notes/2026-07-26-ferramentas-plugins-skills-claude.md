---
title: Claude - Ferramentas, Plugins e Skills
date: 2026-07-26
tags:
  - claude
  - mcp
  - plugins
  - skills
  - integrations
  - notion
  - slack
  - github
  - tools
---

# 26/07/2026 - Ferramentas, Plugins e Skills do Claude

## Comece aqui

- **MCP Servers** - Protocolo padrão aberto criado pela Anthropic para conectar Claude a ferramentas e dados externos de forma segura e padronizada
- **Skills** - Pacotes reutilizáveis que estendem o Claude com conhecimento especializado e workflows específicos da organização
- **Plugins** - Combinam MCP connectors, skills, slash commands e sub-agents em uma unidade compartilhável

---

## Model Context Protocol (MCP) - Visão Geral

O MCP é um protocolo aberto que permite que o Claude se conecte a centenas de ferramentas e fontes de dados externas sem precisar de camadas de automação como Zapier.

**Como funciona:**
- Claude Desktop lança pequenos servidores locais que expõem funções (ler página, criar mensagem, fazer busca)
- Claude aprende a chamá-las quando a demanda o exige
- Usa uma única camada de comunicação unificada entre o LLM e os serviços

**Vantagens:**
- Integração segura e flexível
- Acesso contextual mantendo permissões do usuário
- Padrão único em vez de integrações fragmentadas

### Configuração do MCP

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

---

## MCP Servidores Oficiais

### Notion MCP
- **Acesso:** Leitura e escrita de páginas, bases de dados e blocos
- **Autenticação:** OAuth ou API Key (secret_xxx)
- **Instalação:** `claude mcp add --transport http notion https://mcp.notion.com/mcp`

**Configuração com API Key:**
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "secret_xxxxxxxxxxxx"
      }
    }
  }
}
```

### Slack MCP
- **Acesso:** Ler histórico de canais, escrever mensagens, criar canvas, fazer buscas
- **Escopos necessários:** `channels:history`, `channels:read`, `chat:write`, `users:read`, `search:read`
- **Tokens:** Bot User OAuth Token (começa com `xoxb-`) e Team ID

**Configuração:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-...",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

### GitHub MCP
- Ler repositórios, gerenciar issues/PRs
- Automatizar workflows

### Google Workspace MCP (Community)
- Sheets, Drive, Gmail, Calendar, Docs, Slides, Tasks
- OAuth remoto com instalação em 1 clique

### Supabase MCP
- Conectar Claude a projetos Supabase
- Transports HTTP/SSE com OAuth

---

## Conectores do Claude Desktop

**Acessar:** Claude Desktop → Settings → Connectors → Add

**Opções:**
- **Claude + Notion:** Autorizar via OAuth uma vez, Claude busca, lê, cria e atualiza em todo workspace
- **Claude + Slack:** Requer Pro, Slack pago e aprovação do admin; busca canais, DMs e puxa contexto

---

## Skills - Conhecimento Especializado

### Estrutura de um Skill

Cada skill é um diretório contendo:
1. **skill.md** (obrigatório) - Arquivo principal com frontmatter YAML
2. Arquivos de referência
3. Scripts executáveis
4. Ferramentas customizadas

**Exemplo de frontmatter:**
```yaml
---
name: Nome do Skill
description: Descrição clara de quando Claude deve usar este skill
---
```

### Como Criar

1. Crie uma pasta com o nome do skill
2. Dentro dela, crie `skill.md` com YAML frontmatter
3. Empacote como ZIP (pasta como raiz, não subpasta)
4. Upload em **Customize > Skills > "+ Create skill"**

### Como Usar

1. **Planos:** Disponível em Free, Pro, Max, Team e Enterprise
2. **Ativar:** Navigate to **Settings > Capabilities** (individual) ou **Organization settings > Skills** (Team/Enterprise)
3. **Customizar:** Ir a **Customize > Skills** e ativar/desativar conforme necessário

### Boas Práticas

- Descrição clara indicando quando Claude deve invocar
- Nomes de pasta e título alinhados
- Referenciar arquivos corretamente
- Testar com prompts de exemplo
- Revisar o thinking do Claude para confirmar carregamento

---

## Plugins - Pacotes Reutilizáveis

Plugins combinam:
- **MCP Connectors** - Integração com ferramentas
- **Skills** - Conhecimento especializado
- **Slash Commands** - Comandos (/comando)
- **Sub-agents** - Agentes menores especializados

**Uso:** Tornar Claude especialista em um papel, time ou empresa específico

---

## Integrações Populares

### Notion + Slack + GitHub (Exemplo Real)

É possível criar workflows avançados:
- Claude busca dados do Slack (canais, threads, usuários)
- Processa com contexto do GitHub (PRs, issues, commits)
- Escreve sumários e atualizações no Notion
- Tudo em uma única conversa

**Exemplo:** Sumário mensal de atividade do GitHub → Slack → Notion automaticamente

### Ferramentas de IA Suportadas

- **ChatGPT**
- **Claude**
- **Cursor**
- **Perplexity**
- **Credal AI**
- **Dropbox**
- **Guru**
- **Jasper**
- **Open AI**
- **Notion**
- **Thoughtspot**
- **Wordsmith**
- **Workleap**

---

## Recursos Úteis

- [Model Context Protocol - Documentação Oficial](https://modelcontextprotocol.io/introduction)
- [Claude Code Documentation - MCP](https://code.claude.com/docs/mcp)
- [Awesome Claude Code - Plugins & MCP Servers](https://github.com/jmanhype/awesome-claude-code)
- [Claude Skills Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Slack MCP Guide](https://slack.com/help/articles/48855576908307-Guide-to-Model-Context-Protocol-in-Slack)
- [Notion MCP Setup](https://developers.notion.com/guides/mcp/get-started-with-mcp)