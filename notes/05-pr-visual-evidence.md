# PR Visual Evidence

Use esta skill quando for solicitado adicionar evidências visuais (screenshots, gravações de tela, vídeos de simulador) a um Pull Request no GitHub. O objetivo é documentar visualmente o que foi feito sem sujar o repositório com arquivos binários.

## Referências oficiais

- Gravação via CLI: https://docs.maestro.dev/maestro-flows/workspace-management/record-your-flow.md?displayAgentInstructions=true
- startRecording (in-flow): https://docs.maestro.dev/reference/commands-available/startrecording.md?displayAgentInstructions=true
- stopRecording (in-flow): https://docs.maestro.dev/reference/commands-available/stoprecording.md?displayAgentInstructions=true

## Regras Fundamentais

- **NUNCA** commite screenshots, vídeos ou outros artefatos visuais no repositório git.
- Use **exclusivamente Maestro** para capturar evidências. Dois métodos disponíveis:
  - **CLI (maestro record --local)**: gravação externa do flow inteiro, não-interativa, ideal para evidência de PR.
  - **In-flow (startRecording/stopRecording)**: gravação programática dentro do YAML, ideal para testes de integração que precisam de vídeo como artefato do próprio teste.
- Armazene as capturas em diretórios temporários (`/tmp/pr-visual-evidence-<PR_NUMBER>/`). Artefatos do Maestro ficam em `~/.maestro/tests`.
- Use o browser para abrir o PR no GitHub e faça upload das mídias através do editor de descrição ou comentário temporário.
- No markdown final do PR, use **apenas** URLs hospedadas pelo GitHub: `https://github.com/user-attachments/assets/...`
- Atualize a descrição do PR com `gh pr edit <PR_NUMBER> --body-file /tmp/pr-body.md`.
- Após atualizar, rode `git status --short` e confirme que nenhuma mídia está staged, untracked ou committada no repo.

## Método 1: Gravação via CLI (preferido para evidência de PR)

Use quando precisar gravar um flow existente sem modificá-lo, ou quando a evidência é solicitada após o teste já ter passado.

```bash
# Forma básica — gera MP4 em ~/.maestro/tests/
maestro record --local path/to/YourFlow.yaml

# Com output explícito — salva direto no caminho desejado
maestro record --local path/to/YourFlow.yaml /tmp/pr-visual-evidence-<PR_NUMBER>/evidence.mp4
```

- **Não-interativo**: aceita caminho do flow e output como argumentos diretos. Não abre Studio nem prompt.
- **Rendering local obrigatório**: sempre use `--local`. Remote rendering está deprecated.
- **Limite de 2 minutos**: gravações param automaticamente após 2 minutos. Se o flow for mais longo, divida em múltiplos flows ou use o Método 2.
- **Flags úteis em CI/scripts**: `-e`/`--env` (variáveis de ambiente), `--config`, `--output`, `--repoName`/`--repoOwner`.

## Método 2: Gravação In-Flow com startRecording/stopRecording

Use quando estiver escrevendo ou atualizando testes de integração com Maestro e quiser que o vídeo seja gerado como parte da execução do próprio teste.

### Sintaxe básica

```yaml
appId: yourAppId
---
- launchApp
- startRecording: recording
- tapOn: "Login"
- fillText:
    id: "email"
    text: "test@example.com"
- tapOn: "Submit"
- assertVisible: "Welcome"
- stopRecording
```

O vídeo é salvo como `recording.mp4` relativo ao diretório do flow.

### Sintaxe avançada com path customizado e label

```yaml
- startRecording:
    path: "/tmp/pr-visual-evidence-<PR_NUMBER>/onboarding_flow"
    label: "Evidência visual do fluxo de onboarding"
    optional: true
```

| Parâmetro  | Tipo    | Descrição                                                                 |
|------------|---------|--------------------------------------------------------------------------|
| path       | string  | Caminho do arquivo de gravação, relativo ao diretório do flow.            |
| label      | string  | Label descritivo que aparece no relatório de teste.                       |
| optional   | boolean | Se true, não falha o teste caso a gravação não possa ser iniciada.      |

### Regras importantes

- **Sempre use stopRecording** para finalizar o vídeo. Sem ele, o arquivo não é gerado corretamente.
- stopRecording **não falha** se nenhuma gravação estiver em andamento — seguro para uso condicional.
- Para screenshots pontuais dentro do flow, use `takeScreenshot` entre `startRecording` e `stopRecording` ou fora deles.

## Workflow Completo

1. **Identificar o PR**: use `gh pr view --json number,url,headRefOid` na branch atual, ou peça ao usuário.

2. **Capturar evidências com Maestro**:
   - Escolha o método adequado (CLI para evidência pontual, in-flow para testes de integração).
   - Evite campos sensíveis, tokens, dados pessoais, URLs internas ou PII nas capturas. Prefira dados de teste neutros e valores mascarados.
   - Copie os artefatos para `/tmp/pr-visual-evidence-<PR_NUMBER>/` antes do upload.

3. **Abrir o PR no GitHub via browser**:
   - Use a URL obtida no passo 1.
   - Abra o editor de descrição ou crie um comentário temporário se editar a descrição for complicado.

4. **Upload das mídias via editor do GitHub**:
   - Arraste, cole ou anexe os screenshots/vídeos no editor.
   - Aguarde cada upload completar.
   - Copie as URLs `https://github.com/user-attachments/assets/...` geradas.
   - Mapeie qual URL corresponde a qual captura.

5. **Construir /tmp/pr-body.md**:
   - Inclua resumo conciso do que foi validado visualmente.
   - Embed screenshots com tags HTML:
     ```html
     <img width="390" alt="Descrição curta" src="https://github.com/user-attachments/assets/..." />
     ```
   - Inclua vídeo como link direto (não caminho local).
   - Liste comandos de teste executados e resultados (inclua o flow YAML usado e o método de gravação).
   - Inclua o SHA do commit validado.

6. **Atualizar o corpo do PR**:
   ```bash
   gh pr edit <PR_NUMBER> --body-file /tmp/pr-body.md
   ```

7. **Limpar conteúdo temporário do GitHub**:
   - Se usou comentário temporário apenas para upload, delete-o após copiar as URLs.
   - Não delete os attachments — o corpo do PR depende dessas URLs.

8. **Verificar limpeza do repositório**:
   ```bash
   git status --short
   ```
   - Inspecione por extensões de mídia: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.mp4`, `.mov`, `.webm`, `.m4v`.
   - Se alguma mídia gerada aparecer no repo, remova ou mova para storage temporário antes de finalizar.

## Template do Corpo do PR

Use esta estrutura para `/tmp/pr-body.md` salvo se o PR existente tiver convenção mais forte:

```markdown
## Summary

- Validated <flow ou feature>.
- Confirmed <estado ou comportamento importante>.

## Visual Evidence

<img width="390" alt="<nome da tela ou estado>" src="https://github.com/user-attachments/assets/<id>" />

Video: https://github.com/user-attachments/assets/<id>

## Validation

- Flow: <FlowFile>.yaml
- Recording method: maestro record --local | startRecording/stopRecording
- <command>: passed

## Commit

Validated commit: <commit_sha>
```

Ao preservar descrição existente do PR, mergeie as evidências na estrutura atual em vez de substituir contexto útil. Mantenha o corpo final legível e evite duplicar evidências obsoletas.

## Orientações sobre Upload via Browser

O upload deve acontecer no editor web do GitHub porque ele cria URLs duráveis user-attachments. Não invente URLs de attachment, não aponte markdown para arquivos locais, e não assuma que `gh pr edit` faz upload de mídia. `gh pr edit` aplica apenas o markdown final após o upload via browser ter produzido os links.

Se uploads estiverem lentos, aguarde até o GitHub substituir o placeholder local pela URL `github.com/user-attachments/assets/....` Copie apenas a URL final. Se um arquivo falhar, tente novamente pelo editor antes de editar o corpo do PR.

## Checklist de Segurança

Antes da resposta final, verifique:

- [ ] A URL do vídeo começa com `https://github.com/user-attachments/assets/`.
- [ ] Todo `<img>` usa URL `https://github.com/user-attachments/assets/`.
- [ ] `/tmp/pr-body.md` não contém caminhos locais para screenshots ou vídeos.
- [ ] O vídeo foi gravado com Maestro (`maestro record --local` ou `startRecording/stopRecording`).
- [ ] Se usou `startRecording`, o flow contém `stopRecording` correspondente.
- [ ] O PR foi atualizado com `gh pr edit <PR_NUMBER> --body-file /tmp/pr-body.md`.
- [ ] `git status --short` não mostra mídias geradas no repo.
- [ ] A resposta final reporta: número do PR, commit validado, flow YAML usado, método de gravação, comandos de teste e status limpo do git.
