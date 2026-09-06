---
title: "4 skills que tiram o frontend de IA do genérico: taste, guidelines, DESIGN.md e image-to-code"
description: "Taste Skill, web-design-guidelines da Vercel, awesome-design-md e image-to-code-skill: gosto, filtro de qualidade, design system pronto e tradução de referência visual em código."
date: 2026-09-06
tags:
  - agent-skills
  - ai-agents
  - open-source
  - tools
  - design-systems
layout: post
---

## Carrossel do obrunookamoto sobre plugins de design para agentes

Sequência de posts de Bruno Okamoto (@obrunookamoto) apresentando quatro plugins considerados sensacionais para elevar a qualidade visual do que os agentes de IA geram: um para injetar critério de gosto antes de gerar a UI, um filtro de qualidade com as regras oficiais da Vercel, um sistema de design pronto extraído de sites de referência via DESIGN.md e um tradutor de referência visual em código. A tese do carrossel é que o problema do frontend vibe-coded não se resolve pedindo para "ficar bonito", e sim com gosto explícito, sistema fechado e auditoria antes da produção.

## Taste Skill: o anti-frontend-genérico dos agentes

Skill open-source que injeta critério de gosto no agente: lê o brief, escolhe uma direção de design a partir de referências premium e só então gera a UI. A v2 experimental, reescrita em 2026, infere a direção certa, usa design systems reais quando aplicável e aplica checagem prévia rigorosa para a interface não sair com cara de template. Instalação via `npx skills add Leonxlnx/taste-skill`.

[Acesse a fonte original](https://www.tasteskill.dev/)

## web-design-guidelines: o filtro de qualidade da Vercel

Skill do repositório vercel-labs/agent-skills que puxa as regras oficiais da Vercel (acessibilidade, teclado, formulário, hierarquia) e audita o código da UI contra elas, marcando o que está fraco antes de ir para produção. Uso típico: "review my UI", "check accessibility" ou "audit design". É o filtro de qualidade, não o gerador.

[Acesse a fonte original](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)

## awesome-design-md: design system pronto via DESIGN.md

Coleção curada de análises DESIGN.md de sites de referência. A proposta é copiar um DESIGN.md para o projeto e pedir ao agente uma página com aquela linguagem visual, gerando UI consistente com o sistema. Sem isso, o modelo chuta tom de azul e espaçamento a cada tela; com isso, ele copia um sistema já fechado em vez de improvisar.

[Acesse a fonte original](https://github.com/VoltAgent/awesome-design-md/)

## image-to-code-skill: da referência visual ao código

Skill do mesmo repositório do Taste Skill que traduz referência visual (print, mock, site) em código, preservando o detalhe que some no prompt de texto: alinhamento, densidade, hierarquia. A diretriz central é image-first — gerar as imagens de referência das seções, analisá-las a fundo e implementar o site para corresponder a elas o mais próximo possível, evitando cards dentro de cards e heros genéricos escuros centralizados.

[Acesse a fonte original](https://github.com/Leonxlnx/taste-skill/blob/main/skills/image-to-code-skill/SKILL.md)
