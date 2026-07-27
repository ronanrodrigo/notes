---
title: "PR Visual Evidence"
tags: [github, pr, testing, maestro, documentation]
date: 2026-06-29
---

# 29\/06\/2026 - PR Visual Evidence

Use esta skill quando for solicitado adicionar evidências visuais (screenshots, gravações de tela, vídeos de simulador) a um Pull Request no GitHub. O objetivo é documentar visualmente o que foi feito sem sujar o repositório com arquivos binários.

**Referências oficiais:**

- Gravação via CLI: https:\/\/docs.maestro.dev\/maestro-flows\/workspace-management\/record-your-flow.md?displayAgentInstructions=true

- startRecording (in-flow): https:\/\/docs.maestro.dev\/reference\/commands-available\/startrecording.md?displayAgentInstructions=true

- stopRecording (in-flow): https:\/\/docs.maestro.dev\/reference\/commands-available\/stoprecording.md?displayAgentInstructions=true

## Regras Fundamentais

- **NUNCA** commite screenshots, vídeos ou outros artefatos visuais no repositório git.

- Use **exclusivamente Maestro** para capturar evidências. Dois métodos disponíveis:

  - **CLI (maestro record --local)**: gravação externa do flow inteiro, não-interativa, ideal para evidência de PR.

  - **In-flow (startRecording\/stopRecording)**: gravação programática dentro do YAML, ideal para testes de integração que precisam de vídeo como artefato do próprio teste.

- Armazene as capturas em diretórios temporários (\/tmp\/pr-visual-evidence-<PR_NUMBER>\/). Artefatos do Maestro ficam em ~\/.maestro\/tests.

- Use o browser para abrir o PR no GitHub e faça upload das mídias através do editor de descrição ou comentário temporário.

- No markdown final do PR, use **apenas** URLs hospedadas pelo GitHub: https:\/\/github.com\/user-attachments\/assets\/...

- Atualize a descrição do PR com gh pr edit <PR_NUMBER> --body-file \/tmp\/pr-body.md.

- Após atualizar, rode git status --short e confirme que nenhuma mídia está staged, untracked ou committada no repo.

## Método 1: Gravação via CLI (preferido para evidência de PR)

Use quando precisar gravar um flow existente sem modificá-lo, ou quando a evidência é solicitada após o teste já ter passado.

```bash
# Forma básica — gera MP4 em ~\/.maestro\/tests\/
maestro record --local path\/to\/YourFlow.yaml

# Com output explícito — salva direto no caminho desejado
maestro record --local path\/to\/YourFlow.yaml \/tmp\/pr-visual-evidence-<PR_NUMBER>\/evidence.mp4
```

## Método 2: Gravação In-Flow com startRecording\/stopRecording

Use quando estiver escrevendo ou atualizando testes de integração com Maestro e quiser que o vídeo seja gerado como parte da execução do próprio teste.

## Workflow Completo

1. **Identificar o PR**: use gh pr view --json number,url,headRefOid na branch atual

2. **Capturar evidências com Maestro**

3. **Abrir o PR no GitHub via browser**

4. **Upload das mídias via editor do GitHub**

5. **Construir \/tmp\/pr-body.md**

6. **Atualizar o corpo do PR**

7. **Limpar conteúdo temporário do GitHub**

8. **Verificar limpeza do repositório**

## Checklist de Segurança

Antes da resposta final, verifique:

- [ ] A URL do vídeo começa com https:\/\/github.com\/user-attachments\/assets\/
- [ ] Todo <img> usa URL https:\/\/github.com\/user-attachments\/assets\/
- [ ] \/tmp\/pr-body.md não contém caminhos locais para screenshots ou vídeos
- [ ] O vídeo foi gravado com Maestro
- [ ] git status --short não mostra mídias geradas no repo
