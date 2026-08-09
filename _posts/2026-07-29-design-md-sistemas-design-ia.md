---
title: DESIGN.md — Padrão Aberto para Sistemas de Design com IA
date: 2026-07-29
tags:
  - design-systems
  - ai
  - claudedescription: 'Como usar DESIGN.md para fornecer referências e tokens de design consistentes a agentes de IA.'
---

## Design de IA e o Padrão DESIGN.md

Um post recente de Maick (Nuclear) critica o design gerado por IA como monótono e previsor. O ponto não é capacidade — Claude Code e outros agentes têm poder de design. O problema é **referência**. 

A solução é **DESIGN.md**, um formato aberto do Google que permite descrever um sistema de design inteiro em um único arquivo markdown. Isso permite que IA gere interfaces consistentes e com propósito visual.

O fluxo é simples: escolha uma referência forte → cole o DESIGN.md no Stitch → ajuste ao seu produto → a IA passa a gerar interfaces que seguem um padrão de verdade, não mais "IA genérica".

Quem domina isso está criando produtos que se destacam. O resto continua gerando o mesmo visual de sempre.

[Acesse o post original em X](https://x.com/)

## DESIGN.md: Especificação Oficial

**Google Labs** abriu o código-fonte do DESIGN.md em 21 de abril de 2026 sob Apache 2.0. É um formato Markdown que combina:

- **YAML front matter**: tokens de design legíveis por máquina (cores, tipografia, espaçamento, componentes)
- **Markdown body**: rationale de design (por que cada decisão foi tomada)

A estrutura segue uma ordem canônica: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.

Um DESIGN.md file é um arquivo de texto simples que descreve toda a identidade visual de uma marca em formato que agentes de IA conseguem ler nativamente. Os tokens são a fonte de verdade dos valores. A prosa explica o motivo daqueles valores e quando aplicá-los — e mais importante, quando **não** aplicá-los.

[Acesse a especificação oficial do DESIGN.md](https://github.com/google-labs-code/design.md)

## Refero Styles: Biblioteca Curada de DESIGN.md

Refero Styles extrai sistemas de design de sites reais (Apple, Linear, Stripe, Cursor, ElevenLabs, etc.) e os empacota como arquivos DESIGN.md estruturados. Busque por marca, mood (minimal, editorial, playful, high contrast), cor, tipografia ou URL.

Cada entrada oferece breakdown completo de cores, tipografia, espaçamento e componentes — pronto para copiar o DESIGN.md e colar no contexto do seu agente de IA (Cursor, Claude Code, Windsurf, Lovable, Bolt).

Refero também oferece um **MCP server** que dá aos agentes acesso a 125 mil+ telas reais de produtos e fluxos completos de usuário para estudo antes da geração.

[Acesse Refero Styles](https://styles.refero.design/)

## Neuform: HTML Landing Page Builder com DESIGN.md

Neuform transforma prompts em landing pages HTML com reusáveis DESIGN.md files. Diferente de geradores HTML estáticos, cada output inclui um arquivo DESIGN.md capturado em formato aberto de markdown, pronto para agentes como Claude Code, Cursor ou Lovable construírem sobre ele.

Repositório de templates para estudar padrões de design, remixar direções e manter novas páginas ancoradas em uma clara fonte de verdade.

[Acesse Neuform](https://neuform.ai/)

## getdesign.md: Catálogo de Design Systems

Ferramenta free com 66+ design systems pré-construídos (Stripe, Vercel, Linear, Spotify, SpaceX, Figma, etc.). Instale um arquivo via CLI (`npx getdesign add <slug>`), solte no raiz do projeto, e seu agente de IA segue a linguagem visual.

Cada template inclui:
- **Color tokens**: surface, ink, accent, semantic com valores hex
- **Type scale**: display, heading, body, label com line-height e tracking
- **Spacing & layout**: grid, gutters, container widths, component padding
- **Component patterns**: buttons, cards, navs, forms, modals em prosa que o agente consegue aplicar
- **Motion**: durations, easings, hover e entrance patterns
- **Responsive strategy**: como o sistema collapsa entre breakpoints

O catálogo completo com previews está em getdesign.md.

[Acesse getdesign.md](https://getdesign.md/)

## designmd.ai

Plataforma adicional mencionada para organizar e curar referências de DESIGN.md.
