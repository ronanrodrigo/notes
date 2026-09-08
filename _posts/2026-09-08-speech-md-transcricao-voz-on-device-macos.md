---
title: "speech.md: transcrição de voz 100% on-device no macOS"
description: "Ditados, reuniões e arquivos de áudio transcritos no próprio Mac com SpeechAnalyzer, ScreenCaptureKit e Foundation Models."
date: 2026-09-08
tags:
  - swift
  - open-source
  - tools
  - local-llm
  - ai
  - productivity
layout: post
---

## speech.md

Transcrição de voz para macOS que roda inteiramente no próprio aparelho: sem servidor, sem conta e sem áudio saindo do Mac. Faz ditado com uma tecla em qualquer app, grava reuniões em dois canais (microfone e áudio do sistema, lado a lado) e transcreve arquivos de áudio informando quantas vezes mais rápido que o tempo real rodou. Traz ainda dicionário de atalhos de voz e um refinamento opcional com modelo on-device que transforma listas faladas em bullets. Medido pelo autor em Apple M5: 75x tempo real na transcrição de arquivo, com vocabulário técnico em inglês acertado a custo zero de latência.

[Acesse a fonte original](https://github.com/Andsu-dev/speech.md)

## WWDC25 session 277: SpeechAnalyzer

Sessão oficial da Apple que apresenta o SpeechAnalyzer, o framework que substitui o SFSpeechRecognizer: 100% on-device, sem limite de um minuto por sessão, com resultados entregues como AsyncSequence. É a base técnica que o speech.md usa, com os módulos SpeechTranscriber e SpeechDetector coordenados pelo analisador.

[Acesse a fonte original](https://developer.apple.com/videos/play/wwdc2025/277/)

## Benchmark: SpeechAnalyzer vs Whisper

Primeiro benchmark independente rigoroso (julho de 2026): SpeechAnalyzer marcou 2,12% de word error rate em inglês limpo (LibriSpeech test-clean), superando todas as variantes on-device do Whisper testadas e rodando cerca de 3x mais rápido que o Whisper Small em um M2 Pro. O texto também mostra quando ainda vale escolher Whisper (100+ idiomas, vocabulário customizado) e o buraco de diarização que nenhum dos dois resolve sozinho.

[Acesse a fonte original](https://rohitraj.tech/en/notes/apple-speechanalyzer-vs-whisper-on-device-stt-2026)

## Foundation Models framework

Documentação oficial da Apple do framework que dá acesso ao modelo de linguagem on-device por trás do Apple Intelligence. É o que o speech.md usa nas passagens opcionais de refinamento (formatação Markdown e termos estrangeiros), sem aumentar o tamanho do app e funcionando offline.

[Acesse a fonte original](https://developer.apple.com/documentation/foundationmodels)

## ScreenCaptureKit

Documentação oficial da Apple do framework de captura de áudio e vídeo do sistema. É o que permite ao speech.md capturar o canal dos outros participantes da reunião, com controle fino sobre o que é capturado e entrega via CMSampleBuffer.

[Acesse a fonte original](https://developer.apple.com/documentation/screencapturekit)
