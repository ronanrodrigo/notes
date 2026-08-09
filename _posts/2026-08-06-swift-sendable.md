---
title: "Swift Sendable: Segurança em Concorrência"
description: "Guia sobre o protocolo Sendable em Swift, como garantir segurança em transferência de dados entre domínios de concorrência e prevenir data races."
date: 2026-08-06
tags:
  - automation
  - design-systems
  - security
  - testing
  - mobilelayout:-post
  - mobile
  - swift
---

## Swift Interview Question: What is `Sendable` in Swift?

Infografia completa sobre o protocolo `Sendable`, incluindo conceitos fundamentais, casos de uso, implementação e boas práticas para garantir segurança na transferência de dados entre contextos de concorrência.

A infografia aborda:
- Definição e propósito do protocolo
- Por que Swift introduziu o `Sendable`
- Tipos que conformam automaticamente
- Como tornar uma classe `Sendable`
- Exemplos práticos de código
- Consequências quando uma classe não é `Sendable`
- Padrão mental e dicas de entrevista

## Sendable e @Sendable Closures Explicados com Código

O protocolo `Sendable` indica se a API pública de um valor é thread-safe e pode ser usada com segurança entre domínios de concorrência. Uma API pública é segura quando não possui mutadores públicos, implementa um sistema interno de locking ou usa copy-on-write (comum em tipos de valor). Muitos tipos da biblioteca padrão já conformam a `Sendable`, e o compilador pode inferir conformance implicitamente para tipos customizados.

A conformance deve ocorrer no mesmo arquivo de origem para que o compilador possa verificar todos os membros visíveis. Para classes mutáveis com mecanismos internos de sincronização, use `@unchecked` para indicar que a classe é thread-safe.

[Acesse a fonte original](https://www.avanderlee.com/swift/sendable-protocol-closures/)

## O que significa "Sendable"? – Discussão Swift Forums

A interpretação formal de "Sendable" é "pode ser transferido entre domínios de concorrência". Um tipo é `Sendable` se qualquer programa mutable que acessa não encontra data races. Um tipo pode conformar se: (1) não possui estado mutável, (2) possui estado mutável mas `=` cria uma cópia que não compartilha com o original, ou (3) possui estado mutável mas com sincronização apropriada (como `@MainActor`, copy-on-write, atômicos ou locks privados).

Se um tipo não conforma automaticamente, ele possui propriedades stored cujos tipos não são `Sendable`. A abordagem é auditar cada um individualmente.

[Acesse a fonte original](https://forums.swift.org/t/so-what-does-sendable-mean/54959)

## Dominando Swift Concurrency: Um Guia para Sendable

O protocolo `Sendable` marca tipos que podem ser transferidos com segurança entre limites de concorrência. Tipos de valor como structs e enums conformam facilmente se todas as propriedades são `Sendable`.

Classes requerem mais cuidado:
- Opção 1: Tornar a classe final com propriedades imutáveis
- Opção 2: Usar `@unchecked Sendable` com locks (NSLock, etc.)

Para migrar código existente:
1. Auditar tipos que cruzam limites de actor ou task
2. Começar com tipos de folha simples e avançar para tipos complexos
3. Usar `@preconcurrency` para adoção gradual
4. Ativar "Strict Concurrency Checking" nas configurações de build
5. Converter propriedades mutáveis em imutáveis ou usar actors
6. Testar extensivamente

[Acesse a fonte original](https://medium.com/@mo.fawzy/mastering-swift-concurrency-a-guide-to-sendable-for-ios-developers-04b17d61e36a)

## What is the Sendable Protocol in Swift? | Swift Concurrency #11

O protocolo `Sendable` é simples: indica se um objeto é seguro para enviar em um contexto assíncrono. Para fins práticos, significa se é seguro enviar um objeto para um Actor.

O `Sendable` indica que um valor de um tipo pode ser usado com segurança em código concorrente. Para classes `Sendable`, é essencial que sejam `final` e que todas as propriedades sejam imutáveis.

[Acesse a fonte original](https://www.youtube.com/watch?v=wSmTbtOwgbE)

## Sendable e @Sendable Closures – Disponível a partir de Swift 5.5

A SE-0302 adiciona suporte para "sendable data", dados que podem ser transferidos com segurança para outra thread através do protocolo `Sendable` e do atributo `@Sendable` para funções.

Muitos tipos são inerentemente seguros para enviar: `Bool`, `Int`, `String`, `Array<String>`, `Dictionary<Int, String>` e outros. Para tipos customizados:
- Structs/enums: `Sendable` se contêm apenas valores `Sendable`
- Classes: `Sendable` se herdam apenas de `NSObject` ou nada, todas as propriedades são constantes `Sendable`, e marcadas como `final`
- Closures: Use `@Sendable` para indicar que funcionam concorrentemente

[Acesse a fonte original](https://www.hackingwithswift.com/swift/5.5/sendable)

## Dominando Sendable em Swift 6

Sendable é o sistema de Swift para garantir segurança de dados entre limites de tarefa através de verificações em tempo de compilação. Para conformidade explícita em tipos complexos, marque propriedades como imutáveis ou envolva propriedades mutáveis em actors. Ao conformar, seja preciso: verifique tipos aninhados e se há propriedades mutáveis, considere marcar a classe como `final`.

Para objetos que compartilham estado mutável (cache, session handler), use um actor para torná-lo `Sendable`.

[Acesse a fonte original](https://medium.com/@wesleymatlock/mastering-sendable-in-swift-6-e13d04d86820)

## Enviando vs. @Sendable em Swift 6

O `@Sendable` em closures ajuda o compilador a garantir que certos closures capturem apenas estado que pode ser usado com segurança de múltiplas tasks ou contextos de isolamento.

Swift 6 introduz a keyword `sending` que pode ser aplicada a closures, permitindo que o compilador garanta que estado capturado não seja acessado após ser transferido para novo contexto.

[Acesse a fonte original](https://www.youtube.com/watch?v=Ka28hay60VQ)

## Regra Prática para Conformar a Sendable

1. Padrão para **Structs** ou **Enums**
2. Para estado mutável compartilhado, use um **Actor**
3. Para estado imutável compartilhado, use uma **classe final com propriedades `let`**
4. Use **`@unchecked Sendable`** apenas se implementar manualmente locks de thread e documentar a sincronização

[Acesse a fonte original](https://www.abhishekshukla.dev/blog/sendable-explained/)

## Entendendo Sendable em Swift: Dominando Segurança de Concorrência

Um "domínio de concorrência" em Swift é um contexto de execução isolado, como um Actor ou Task. Quando você passa um objeto de um domínio para outro (ex: em `Task.detached` ou enviando para um actor), cruza um limite. `Sendable` é um protocolo marcador que diz ao compilador: "Este tipo é seguro para ser compartilhado concorrentemente."

Tipos de valor são inerentemente seguros porque são copiados quando passados. Se um struct ou enum é composto inteiramente de propriedades `Sendable`, Swift implicitamente torna o struct inteiro `Sendable`. Tipos de referência (classes) não são implicitamente `Sendable` porque compartilham referência.

[Acesse a fonte original](https://www.abhishekshukla.dev/blog/sendable-explained/)

## Post publicado

[Acesse o post no site](https://ronanrodrigo.dev/notes/2026/08/06/swift-sendable.html)
