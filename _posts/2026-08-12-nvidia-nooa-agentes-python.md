---
title: "NVIDIA NOOA: Agentes como Classes Python Nativas"
description: "Curadoria sobre NOOA, framework open source da NVIDIA que simplifica construção de agentes integrando engenharia de agentes com engenharia de software através de classes Python."
date: 2026-08-12
tags:
  - ia
  - agentes
  - python
  - engineering
  - nvidia
  - framework
---

## NVIDIA NOOA: Agentes como Classes Python Nativas

Essa é a ideia por trás do NVIDIA-labs OO Agents, um framework open source desenvolvido pela NVIDIA. A proposta é radical: em vez de separar prompts, ferramentas, callbacks e workflows em abstrações distintas, o agente é definido como uma única classe Python.

Coloque tudo isso dentro de um objeto Python:
- Estado → atributos do objeto
- Capacidades → métodos Python
- Prompts → docstrings
- Contratos → type annotations
- Comportamento agentic → métodos implementados pelo LLM

Um método Python tradicional continua determinístico. Já um método com `...` pode ser executado pelo LLM como um método agentic, permitindo que o modelo complete a implementação em tempo de execução.

[Acesse o repositório oficial no GitHub](https://github.com/NVIDIA-NeMO/labs-OO-Agents)

## Arquitetura e Características Principais

NOOA unifica seis conceitos emergentes em uma única superfície:

**Typed Input/Output**: Entradas e saídas são fortemente tipadas e validadas em tempo de execução.

**Pass-by-Reference**: Modelos podem agir sobre objetos Python vivos em vez de serialização de texto achatada.

**Code as Action**: O modelo realiza ações escrevendo código Python normal, não chamadas de ferramentas rígidas baseadas em schema.

**Programmable Loop Engineering**: Dois estratégias de execução: `PredictStrategy` para chamadas LLM tipadas únicas com retry local, e `CodeActStrategy` que oferece um Python REPL iterativo.

**Explicit Object State**: O agente possui estado durável e explícito, não apenas contexto de conversa.

**Model-Callable Harness APIs**: O modelo pode inspecionar contexto e eventos através de APIs Pythônicas.

[Leia o paper completo no arXiv](https://arxiv.org/abs/2607.20709)

## Integração de Agent Engineering + Software Engineering

O que torna NOOA especialmente interessante não é apenas mais um framework de agentes. É a tentativa de aproximar agent engineering e software engineering em uma mesma abstração.

Você deixa de construir apenas um "workflow de IA". Passa a construir um objeto de software que possui capacidades agentic, mantendo toda a infraestrutura que a engenharia de software já sabe fazer bem:

- Tipagem de dados
- Testes unitários
- Rastreamento de execução
- Refatoração de código
- Versionamento
- Code review

[Leia sobre agentes como objetos Python no byteiota](https://byteiota.com/nvidia-nooa-build-ai-agents-as-plain-python-classes/)

## Desempenho e Eficiência

NVIDIA reporta resultados impressionantes em benchmarks:

- **SWE-bench Verified**: 82.2% com GPT-4o
- **CyberGym L1**: 86.8%
- **ARC-AGI-3**: 85.1% mean RHAE
- **Eficiência de tokens**: ~metade dos tokens de outros harnesses comparáveis (~1.1M tokens vs 2.2M em abordagens similares)

[Confira a análise detalhada no AI Tools Recap](https://aitoolsrecap.com/Blog/nvidia-nooa-python-agent-framework-review-2026)

## Instalação e Uso

NOOA está disponível sob licença Apache 2.0 e requer Python 3.12–3.13:

```bash
pip install nooa          # core framework
pip install nooa-cli      # CLI tools e trace viewer
pip install nooa-memory   # subsistema de memória de longo prazo
```

É agnóstico de modelo e funciona com qualquer backend suportado por LiteLLM: OpenAI, Anthropic, Ollama, vLLM e qualquer endpoint compatível com OpenAI.

## Primeiros Passos

Tutorial prático de construção de um agente NOOA:

[Build Your First Object-Oriented Agent](https://alessiodevoto.github.io/Your-First-Object-Oriented-Agent/)

## Status e Disponibilidade

- **Versão**: v0.0.8 (lançada em 30 de julho de 2026)
- **Status**: Research preview / alpha (não recomendado para workloads em produção regulada)
- **Licença**: Apache 2.0
- **Repositório**: [NVIDIA-NeMO/labs-OO-Agents](https://github.com/NVIDIA-NeMO/labs-OO-Agents)
- **Comunidade**: Atingiu mais de 1.300 GitHub stars dias após o lançamento

[Leia o anúncio completo no MarketechPost](https://www.marktechpost.com/2026/08/07/nvidia-ai-releases-nooa-an-object-oriented-python-framework/)