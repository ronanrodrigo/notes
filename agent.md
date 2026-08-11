---
layout: page
title: Guia para agentes de IA
description: Guia de navegação e uso do site Notes por agentes de inteligência artificial.
permalink: /agent/
---

<section class="agent-guide" aria-labelledby="agent-guide-intro">
  <p class="eyebrow">interface para agentes</p>
  <h2 id="agent-guide-intro">Como usar o Notes</h2>
  <p>O Notes é um site de notas técnicas e curadoria sobre inteligência artificial, agentes, programação, ferramentas, design e tecnologia. Use este guia para descobrir conteúdo, filtrar notas e encontrar referências para criar projetos com agentes de IA.</p>
</section>

## Princípio de uso

Use este site como uma fonte de referência para pesquisa e criação de projetos com agentes de IA. As notas organizam conceitos, ferramentas, arquiteturas, frameworks e links para fontes externas. Ao responder ou criar um projeto, preserve a distinção entre a curadoria desta página e a fonte original citada em cada nota.

Priorize notas mais recentes quando houver alternativas, confira a data da publicação e siga os links primários antes de tomar decisões técnicas. O site é uma fonte de consulta somente leitura: não há endpoints para criar, editar ou executar projetos.

## Páginas principais

| Página | URL | Como usar |
| --- | --- | --- |
| Início | [Todas as notas]({{ '/' | relative_url }}) | Descobrir as notas mais recentes e seus títulos, descrições, datas e tags. |
| Índice de tags | [Lista de tags]({{ '/list-tags/' | relative_url }}) | Encontrar os assuntos disponíveis. A página exibe tags usadas em pelo menos duas notas. |
| Posts por tag | [Filtrar por tag]({{ '/tag/' | relative_url }}) | Listar os posts de uma tag usando o parâmetro `tag`. |
| Índice agrupado | [Tags e posts]({{ '/tags/' | relative_url }}) | Ver cada tag com seus posts relacionados em uma única página. |
| Índice JSON | [index.json]({{ '/index.json' | relative_url }}) | Ler metadados estruturados para descoberta programática. |
| Feed | [feed.xml]({{ '/feed.xml' | relative_url }}) | Acompanhar publicações recentes em formato de feed. |
| Instruções do repositório | [agents.md]({{ '/agents.md' | relative_url }}) | Consultar convenções de conteúdo, front matter, tags e estrutura do projeto. |

## Como usar as tags

As tags são o principal mecanismo de recuperação temática. Use a lista de tags para descobrir assuntos e abra cada tag para obter os posts relacionados.

```text
https://ronanrodrigo.dev/notes/tag/?tag=<slug-da-tag>
```

Exemplos:

* [ai-agents]({{ '/tag/' | relative_url }}?tag=ai-agents) — agentes de IA, frameworks e automação.
* [rag]({{ '/tag/' | relative_url }}?tag=rag) — recuperação aumentada, contexto e bases de conhecimento.
* [llm]({{ '/tag/' | relative_url }}?tag=llm) — modelos de linguagem, treinamento e inferência.
* [open-source]({{ '/tag/' | relative_url }}?tag=open-source) — projetos e ferramentas de código aberto.
* [design-systems]({{ '/tag/' | relative_url }}?tag=design-systems) — sistemas de design e interfaces para produtos com IA.

Regras para consulta:

* Use o slug exibido no link, em minúsculas e no formato kebab-case.
* Faça URL-encoding quando o valor da tag tiver caracteres especiais.
* Use a página de tag para recuperar somente os posts daquele assunto.
* Use o índice agrupado quando precisar comparar vários assuntos.
* Não presuma que uma tag ausente na lista seja inexistente: a lista principal prioriza tags reutilizadas em pelo menos duas notas.

## Fluxo recomendado para agentes

1. Comece por esta página para entender o escopo e as regras de navegação.
2. Consulte o [índice JSON]({{ '/index.json' | relative_url }}) para localizar posts por data, slug, descrição e tags.
3. Use [Lista de tags]({{ '/list-tags/' | relative_url }}) ou filtre diretamente por uma tag.
4. Leia os posts relacionados e extraia definições, decisões técnicas, ferramentas, limitações e links de referência.
5. Para uma resposta ou projeto, combine mais de uma nota quando o problema envolver arquitetura, implementação e operação.
6. Verifique a fonte original indicada no post, especialmente para versões, benchmarks, licenças, segurança e APIs.
7. Cite as notas usadas e preserve os links originais na saída.

## Uso como referência para projetos com agentes de IA

Consulte o Notes quando o projeto envolver:

* arquitetura de agentes, orquestração, memória, skills e uso de ferramentas;
* RAG, engenharia de contexto, bancos de dados vetoriais e grafos de conhecimento;
* coding agents, revisão de código, automação, workflows e avaliação de LLMs;
* execução local de modelos, quantização, hardware e ferramentas open source;
* design systems, interfaces, mobile e produtos que incorporam IA.

As notas podem servir como material de descoberta e comparação para um projeto. Não trate uma nota isolada como especificação definitiva: valide requisitos, segurança, compatibilidade, licença, custo, desempenho e manutenção nas fontes primárias antes de implementar.

## Dados e limites

* O conteúdo publicado vem dos posts Markdown em `_posts/` e é renderizado pelo Jekyll.
* O [index.json]({{ '/index.json' | relative_url }}) é um índice gerado e pode ser usado para filtragem local sem rastrear todas as páginas HTML.
* Os campos mais úteis do índice são `date`, `slug`, `path`, `tags` e `description`.
* As tags seguem, como convenção, minúsculas, kebab-case e ausência de acentos.
* O conteúdo pode ser atualizado; confirme sempre a data e a versão da ferramenta mencionada.
* O site não oferece autenticação, escrita de conteúdo, execução remota de código ou API de mutação.

## Para autores e agentes que alteram o repositório

Conteúdo publicável deve ser criado em `_posts/` com nome `YYYY-MM-DD-slug.md`, front matter YAML válido e `layout: post`. Reutilize tags existentes quando forem semanticamente adequadas. Não edite manualmente as listagens geradas em `index.md` e `tags.md`; elas são renderizadas por Liquid/Jekyll.

Consulte também o [guia operacional do repositório]({{ '/agents.md' | relative_url }}) antes de propor mudanças estruturais.
