---
title: Kimi K3 local com Unsloth Dynamic
date: 2026-07-29
tags:
  - kimi-k3
  - unsloth
  - gguf
  - quantization
  - local-llm
  - hardware
---

## Run KIMI K3 Locally (Unsloth Dynamic)

Guia da Unsloth mostrando como rodar o Kimi K3 localmente usando quantizações dinâmicas. O modelo original é 2.8T parâmetros (~1,56 TB em precisão cheia), mas com as quantizações dinâmicas consegue reduzir significativamente o tamanho mantendo acurácia alta.

- **Dynamic 1-bit**: ~78,9% top-1 accuracy, ~594–620 GB de memória (RAM+VRAM ou unified)
- **Dynamic 2-bit**: ~90% top-1 accuracy, ~861 GB
- **Q8 (Lossless)**: precisão total, ~1,6 TB
- Execução: Unsloth Studio, llama.cpp
- Hardware: Mac Studio com 128GB RAM + offloading, ou DGX Stations

[Acesse o guia original da Unsloth](https://unsloth.ai/docs/models/kimi-k3)

## Guia Kimi K3 em Japonês

Versão em japonês do guia oficial, com tabelas detalhadas de requisitos de hardware para as variantes S, M, XXS e XL das quantizações dinâmicas 1-bit e 2-bit.

[Acesse a versão em japonês](https://unsloth.ai/docs/jp/moderu/kimi-k3)

## Unsloth GGUF Repository

Repositório oficial no Hugging Face com os arquivos GGUF pré-quantizados do Kimi K3, prontos para usar com Unsloth Studio ou llama.cpp.

[Acesse o repositório de GGUFs](https://huggingface.co/unsloth/Kimi-K3-GGUF)

## Unsloth GGUF – Instruções e Setup

Seção do Hugging Face com instruções passo-a-passo para instalar Unsloth Studio, baixar os modelos GGUF e começar a rodar o Kimi K3 localmente em macOS, Linux, WSL e Windows.

[Acesse as instruções de setup](https://huggingface.co/unsloth/Kimi-K3-GGUF/tree/main)
