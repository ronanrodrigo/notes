# AGENTS.md — Instruções Oficiais de Criação

Instruções compiladas de fontes oficiais: GitHub Copilot, OpenAI Codex, Claude Code, Cursor e outros agentes de IA.

---

## O que é AGENTS.md?

Um arquivo Markdown na raiz do repositório que serve como **README para agentes de IA**. Define contexto, instruções e preferências que o agente precisa para trabalhar efetivamente no projeto.

**Suportado por**: GitHub Copilot, Claude Code, OpenAI Codex, Cursor, Aider, e outras ferramentas de IA.

---

## Estrutura Recomendada

**Tamanho ideal**: 100-200 linhas (máximo 300)

### 1. **Project Overview** (Obrigatório)
```markdown
# AGENTS.md

> [Uma frase descrevendo o projeto] usando [Stack técnico com versões]
```
**Exemplo:**
> This is a TypeScript CLI tool for Next.js projects using Node 22, TypeScript 5.3, and Vitest.

### 2. **Tech Stack** (Obrigatório)
Seja específico com versões:
```markdown
## Tech Stack
- Node.js 22.x
- TypeScript 5.3+
- React 18 + Vite 5.x
- Tailwind CSS 3.x
- Vitest for testing
```

### 3. **Build & Test Commands** (Obrigatório - maior impacto)
**CRÍTICO**: Coloque aqui ANTES de qualquer coisa.
```markdown
## Commands

### Setup
\`\`\`bash
npm install
# or
pnpm install
\`\`\`

### Development
\`\`\`bash
npm run dev
\`\`\`

### Testing
\`\`\`bash
npm test              # Run all tests
npm run test:watch   # Watch mode
npm run coverage     # Coverage report
\`\`\`

### Linting & Type Checking
\`\`\`bash
npm run lint         # Run ESLint
npm run type-check   # TypeScript check
npm run format       # Prettier format
\`\`\`

### Build
\`\`\`bash
npm run build        # Production build
\`\`\`
```

**Regra**: Inclua flags e opções completas, NÃO apenas nomes de ferramentas.

### 4. **Project Structure** (Recomendado)
```markdown
## Directory Structure
- `/src` — Source code
  - `/src/components` — React components
  - `/src/services` — Business logic
  - `/src/utils` — Helper functions
- `/tests` — Test files
- `/docs` — Documentation
- `/scripts` — Build scripts
```

### 5. **Code Style & Conventions** (Recomendado)
**Use exemplos reais, NÃO explicações abstratas:**

```markdown
## Code Style

### Good Example
\`\`\`typescript
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
\`\`\`

### Anti-pattern (Avoid)
\`\`\`typescript
function calc(i) {
  let t = 0;
  for (let x = 0; x < i.length; x++) {
    t = t + i[x].p;
  }
  return t;
}
\`\`\`

### Conventions
- Use descriptive names (no abbreviations)
- Prefer const/let over var
- Keep functions under 30 lines
- Write JSDoc for public functions
- Use TypeScript strict mode
```

### 6. **Boundaries (Always / Ask First / Never)** (Obrigatório)
```markdown
## Boundaries

### Always
- Modify `/src` and `/tests` directories
- Run validation commands before suggesting changes
- Write tests for new features
- Follow commit message format: \`type(scope): message\`

### Ask First
- New dependencies or major upgrades
- Database migrations
- CI/CD workflow changes
- Infrastructure changes

### Never
- Commit secrets or API keys
- Delete test files
- Modify \`package-lock.json\` directly
- Touch vendor/ or node_modules/
- Alter environment configuration files
```

### 7. **Testing Requirements** (Recomendado)
```markdown
## Testing

- Framework: Vitest
- Coverage goal: 80% or higher
- Location: `/tests` directory
- Run \`npm test\` before committing
- Integration tests in `/tests/integration`
- Unit tests in `/tests/unit`
```

### 8. **Git Workflow** (Recomendado)
```markdown
## Git Workflow

1. Create a feature branch: \`git checkout -b feature/my-feature\`
2. Commit using Conventional Commits: \`feat: add new component\`
3. Push and create a Draft PR
4. Ensure all tests pass: \`npm test\`
5. Mark as "Ready for Review"

### Conventional Commits
- \`feat:\` New feature
- \`fix:\` Bug fix
- \`docs:\` Documentation
- \`test:\` Tests
- \`chore:\` Build, dependencies
```

### 9. **Critical Files & Entry Points** (Opcional)
```markdown
## Important Files
- Entry point: \`src/index.ts\`
- Config: \`vite.config.ts\`
- Type definitions: \`src/types/\`
- API routes: \`src/api/\` (if applicable)
```

### 10. **Common Gotchas** (Recomendado)
```markdown
## Common Pitfalls

### Issue: Tests fail with "Cannot find module"
**Cause**: TypeScript compiled but not bundled
**Fix**: Run \`npm run build\` before testing

### Issue: Prettier conflicts with ESLint
**Cause**: Not running \`npm run format\` after lint
**Fix**: Always run \`npm run lint && npm run format\`
```

---

## Template Mínimo (para projetos novos)

```markdown
# AGENTS.md

> [Uma linha: o que é este projeto e stack]

## Tech Stack
- [Linguagem] [versão]
- [Framework] [versão]
- [Ferramentas principais]

## Commands
\`\`\`bash
npm install
npm run dev
npm test
npm run build
npm run lint
\`\`\`

## Boundaries
### Always
- Modify src/ e tests/
- Run validation before changes

### Ask First
- New dependencies
- Infrastructure changes

### Never
- Commit secrets
- Modify generated files
```

---

## Onde Colocar

- **Preferido**: Raiz do repositório `/AGENTS.md` (maiúsculo)
- **Alternativas**: `/agents.md`, `/.well-known/agents.md`, `/docs/AGENTS.md`
- **Monorepos**: Arquivo raiz + arquivos aninhados em cada package

---

## Dicas Oficiais

✅ **FAÇA:**
- Coloque comandos ANTES de explicações
- Use exemplos reais do seu código
- Seja específico (versões, flags completas)
- Mantenha sob 200 linhas
- Atualize quando a estrutura mudar

❌ **NÃO FAÇA:**
- Descrições vagas ("use React" → "React 18 with TypeScript + Vite 5")
- Comandos sem flags (npm test → npm test -- --coverage)
- Explicações abstratas (use snippets reais)
- Deixar ficar > 300 linhas
- Copiar exemplos de outros projetos

---

## Validação

Use a ferramenta oficial: https://agent-ready.dev

Seu AGENTS.md deve ter pelo menos **2 de 3**:
- ✅ Comandos de instalação/build/teste
- ✅ Detalhes de configuração
- ✅ Exemplos de uso

---

## Para Claude Code (CLAUDE.md)

Se quiser instruções específicas para Claude:

**Opção 1**: Referenciar AGENTS.md
```markdown
# CLAUDE.md

@AGENTS.md

## Claude-specific instructions
[conteúdo adicional específico]
```

**Opção 2**: Symlink
```bash
ln -s AGENTS.md CLAUDE.md
```

---

## Fontes Oficiais

- https://github.com/agentsmd/agents.md (especificação aberta)
- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/ (GitHub oficial)
- https://docs.github.com/en/copilot/reference/custom-agents-configuration (GitHub Copilot docs)
- https://agent-ready.dev/how-to-write-an-effective-agents-md (Agent Ready)
- https://developers.openai.com/codex/guides/agents-md.md (OpenAI Codex)