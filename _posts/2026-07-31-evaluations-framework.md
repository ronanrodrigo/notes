---
title: "Evaluations Framework — Avaliação sistemática de recursos com IA"
description: "Framework da Apple para medir qualidade de features com IA/LLM em Swift, integrando com testes de CI usando datasets, métricas e model-as-judge."
date: 2026-07-31
tags:
  - testing
  - llm
  - ai-agents
  - tools
  - automation
  - design-systems
  - mobile
  - prompt-engineering
  - githublayout: post
---

## Apple Evaluations Framework (WWDC26)

**O que é:** Framework Swift da Apple para **medir sistematicamente a qualidade de recursos alimentados por IA** em aplicativos—usando **datasets + métricas + agregação** integrado diretamente no fluxo de desenvolvimento e testes. Corre dentro do **Swift Testing** (permitindo gates de CI), suportando verificações simples de aprovação/falha e padrões mais sofisticados de **"modelo como juiz"** para avaliação qualitativa.

[Acesse a documentação da Apple](https://developer.apple.com/documentation/evaluations)

## Por que não usar unit tests tradicionais

Recursos com IA quebram o contrato fundamental dos testes de software: a mesma entrada pode produzir saídas diferentes. Você não pode usar `#expect(output == "exact string")` em modelos generativos. O Evaluations framework trata a qualidade de IA como algo a medir **estatisticamente** em vez de afirmar exatamente—mais como benchmarking de performance do que testes unitários.

## Os 5 passos para construir uma avaliação

1. **Subject**: Defina qual código está sendo medido
2. **Dataset**: Use array de `ModelSample` com inputs (e opcionalmente valores esperados/referência)
3. **Metrics & Evaluators**: Defina o que medir (contagem de tags, comprimento, sentimento) e como pontuar (pass/fail)
4. **AggregateMetrics**: Resuma os resultados em estatísticas resumidas (média, desvio padrão, taxa de aprovação)
5. **Test com Swift Testing**: Execute a avaliação como `@Test` com o trait `.evaluates`, use `#expect` em valores agregados para criar um gate de CI

[Assistir Meet the Evaluations framework](https://developer.apple.com/videos/play/wwdc2026/298/)

## Como integrar com Swift Testing e CI

As avaliações se integram ao Swift Testing através de um trait de teste. Durante o teste, você acessa os resultados da avaliação e usa **assertions `#expect` em valores agregados** (ex: pontuação média ou taxa de aprovação) para criar um gate de execução em CI. Exemplo de gate:

```swift
@Test(.evaluates(evaluation, info: evaluationInfo))
func expenseTagsStayAccurate() async throws {
  let result = EvaluationContext.current.result
  let score = result.aggregateValue(.mean(of: tagCountMetric))
  #expect(score >= 0.85)
}
```

[Ver documentação de Swift Testing com .evaluates trait](https://developer.apple.com/documentation/evaluations)

## Componentes-chave na prática

### ModelSample
Representa um **input para avaliação** (e opcionalmente um valor esperado/referência). É a unidade básica do seu dataset.

### ModelJudgeEvaluator
Um **modelo como juiz**—um modelo de linguagem que pontua as saídas com uma **escala de pontuação configurável** (numérica, pass/fail, customizada) e opcionalmente instruções específicas do domínio. Aplica julgamentos subjetivos de forma consistente em todo o dataset.

[Customizing the Pointwise Model-as-Judge Prompt](https://developer.apple.com/documentation/Evaluations/scoring-with-model-as-judge-evaluators)

### SampleGenerator
Ajuda a **evitar datasets apenas com autoria manual** sintetizando mais amostras de um **conjunto seminal** usando o modelo de sua escolha. Datasets robustos têm milhares de amostras com variedade; a mão não escala, então `SampleGenerator` sintesiza mais amostras a partir de alguns seeds.

[Meet the Evaluations framework — SampleGenerator](https://developer.apple.com/videos/play/wwdc2026/298/)

### ToolCallEvaluator (para apps agentic)
Para aplicativos que usam agent e tool-calling, você pode verificar se um agent produz a **trajetória esperada de chamadas de ferramentas** usando `TrajectoryExpectation` e `ToolCallEvaluator`. Isto combina uma `LanguageModelSession` com as ferramentas, captura a transcrição estruturada e relata junto com outras avaliações no Xcode.

[Create robust evaluations for agentic apps (Session 299)](https://developer.apple.com/videos/play/wwdc2026/299/)

## Quando usar vs evitar

### Use quando:
- ✅ **Capturando regressões de prompt/modelo em CI**—detectar degradação antes do envio
- ✅ **Avaliação fuzzy/qualitativa**—pontuação de saída com model-as-judge
- ✅ **Validação de comportamento de tool-calling do agente**—verificar que ferramentas corretas são chamadas
- ✅ **Comparação de estratégias de prompt**—rodar duas avaliações lado a lado

### Evite quando:
- ❌ **Lógica determinística**—já coberta por assertions simples de Swift Testing
- ❌ **Datasets minúsculos**—hand-picked com poucas amostras (resultados podem não ser significativos)
- ❌ **XCTest targets**—o trait `.evaluates` é específico de Swift Testing
- ❌ **Em lugar de testes unitários básicos**

[Meet the Evaluations framework — Avoid cuando section](https://developer.apple.com/videos/play/wwdc2026/298/)

## Tip: SampleGenerator não é treinável manualmente

Use `SampleGenerator` para **sintetizar mais amostras automaticamente** de um conjunto seminal. Não tente calibrar/treinar o gerador manualmente—use **worked examples** para calibrar o **model judge** (o avaliador), não o gerador de amostras.

[Improve your prompts by hill-climbing with Evaluations (Session 335)](https://developer.apple.com/videos/play/wwdc2026/335/)

## Avaliação de model judge com Cohen's κ

Ao usar um model judge, compare suas pontuações com as de um avaliador humano especialista usando **Cohen's κ (kappa)** em vez de precisão simples quando distribuições de score são irregulares. Isso valida que o juiz está alinhado com o padrão ouro humano.

[WWDC 2026: Improve your prompts by hill-climbing with Evaluations](https://wwdc.ai/2026/335/)

## Framework disponível em

- iOS 27
- iPadOS 27
- macOS 27
- watchOS 27
- visionOS 27
- **Não** em tvOS

É um **framework de tempo de desenvolvimento/teste**—você o vincula a partir do seu alvo de teste, não é distribuído dentro da app.

[Axiom — Claude Code Agents for iOS Development](https://charleswiltgen.github.io/Axiom/reference/foundation-models-evaluations-ref)

## Recursos adicionais

- **Documentação oficial**: [Apple Developer Documentation — Evaluations](https://developer.apple.com/documentation/evaluations)
- **Meet the Evaluations framework (298)**: [Vídeo WWDC26](https://developer.apple.com/videos/play/wwdc2026/298/)
- **Create robust evaluations for agentic apps (299)**: [Vídeo WWDC26](https://developer.apple.com/videos/play/wwdc2026/299/)
- **Improve your prompts by hill-climbing (335)**: [Vídeo WWDC26](https://developer.apple.com/videos/play/wwdc2026/335/)
- **Axiom Reference**: [Foundation Models & Evaluations](https://charleswiltgen.github.io/Axiom/reference/foundation-models-evaluations-ref)
- **ByteIOTA Article**: [Apple Evaluations Framework: Measure iOS AI Feature Quality](https://byteiota.com/apple-evaluations-framework-measure-ios-ai-feature-quality/)
- **Blake Crosley Blog**: [Evaluations: XCTest for Model Quality (iOS 27)](https://blakecrosley.com/blog/apple-evaluations-framework)
