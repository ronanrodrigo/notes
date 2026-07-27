---
title: MarkItDown — convertendo documentos para Markdown
date: 2026-07-27
tags:
  - markitdown
  - microsoft
  - conversao-documentos
  - claude
  - ia
  - markdown
  - python
---

## MarkItDown — Microsoft resolve o problema de processar documentos para Claude

**Publicação:** Rafa Grandi (@rafa.grandi) — Instagram

**Contexto da curadoria:**

Segundo Rafa Grandi, quando você envia um arquivo para Claude, ele precisa ler o documento inteiro, o que consome muitos tokens. Um simples PDF pode gastar até 70 mil tokens apenas para leitura. Microsoft lançou uma ferramenta gratuita chamada **MarkItDown** que resolve esse problema convertendo documentos (Word, Excel, PowerPoint, vídeos do YouTube) em arquivos `.md` muito mais leves e fáceis para Claude processar.

A ferramenta já tem mais de 100 mil likes no GitHub e está em desenvolvimento ativo.

## MarkItDown — Conversor universal de documentos para Markdown

**Fonte:** Microsoft (GitHub e documentação oficial)

MarkItDown é um utilitário Python leve desenvolvido pela equipe AutoGen da Microsoft, projetado para converter múltiplos formatos de arquivo em Markdown, preservando estrutura, títulos, listas, tabelas e links.

**Formatos suportados:**
- PDF (incluindo documentos escaneados com OCR)
- Word (.docx)
- PowerPoint (.pptx)
- Excel (.xlsx)
- Imagens (EXIF metadata e OCR)
- Áudio (transcrição automática de fala)
- Vídeos do YouTube (extração de legendas e transcrição)
- HTML
- E-books (EPUB)
- Dados estruturados (CSV, JSON, XML)
- Arquivos ZIP (processa conteúdo interno)

[Acesse o repositório no GitHub](https://github.com/microsoft/markitdown)

## MarkItDown para VS Code — Extensão integrada

**Fonte:** Visual Studio Marketplace

Existe uma extensão oficial para VS Code que permite converter documentos com um clique direito no editor, sem necessidade de configuração adicional além de ter Python na PATH.

[Acesse a extensão](https://marketplace.visualstudio.com/items?itemName=bioinfo.markitdown-vscode)

## Como usar MarkItDown na prática

**Fonte:** Documentação Microsoft e tutoriais comunitários

**Instalação:**
```bash
pip install markitdown
```

**Conversão simples via linha de comando:**
```bash
markitdown documento.pdf > saida.md
markitdown documento.pdf -o saida.md
markitdown relatorio.xlsx -o relatorio.md
```

**Integração com Claude via MCP:**
```bash
pip install markitdown-mcp
```

Com `markitdown-mcp`, Claude Desktop e Claude Code podem chamar conversão de documentos automaticamente. Basta pedir ao Claude para "ler este PDF" e a conversão acontece nos bastidores.

**Uso como biblioteca Python:**
```python
from markitdown import MarkItDown

md = MarkItDown()
resultado = md.convert("exemplo.xlsx")
print(resultado.text_content)
```

[Acesse a documentação completa](https://github.com/microsoft/markitdown)

## O impacto na eficiência com LLMs

**Insights extraídos de discussões e análises da comunidade**

O ganho de eficiência é significativo: converter documentos para Markdown antes de enviar para Claude reduz drasticamente o consumo de tokens, permitindo processar mais informação com menos custo. É particularmente útil para:

- Indexação de documentos
- Preparação de dados para fine-tuning
- Construção de sistemas RAG (Retrieval-Augmented Generation)
- Análise de texto estruturado
- Processamento em batch de múltiplos formatos

[Acesse repositório oficial](https://github.com/microsoft/markitdown)
