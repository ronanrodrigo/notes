#!/usr/bin/env python3
"""Apply a reviewed semantic taxonomy, then remove singleton tags globally."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

POSTS = Path(__file__).resolve().parents[1] / "_posts"

# Tags describe the subject of each post, not implementation words found in its body.
TAGS = {
"2026-05-28-ciclo-criado-pela-ia.md": ["workplace", "productivity", "society"],
"2026-07-23-agents-oficiais-criacao.md": ["ai-agents", "documentation", "github"],
"2026-07-23-como-criar-agents.md": ["ai-agents", "documentation", "github"],
"2026-07-23-repos-ia-github-trending.md": ["ai", "github", "open-source"],
"2026-07-23-self-host-ia-coolify-agentes-rag.md": ["self-hosting", "ai-agents", "rag", "open-source"],
"2026-07-23-trilhas-cursos-ia.md": ["ai", "learning", "prompt-engineering", "ai-agents"],
"2026-07-23-turbovec-turboquant.md": ["vector-database", "rust", "rag", "quantization"],
"2026-07-24-colibri-motor-local-ia.md": ["local-llm", "rust", "llm", "open-source"],
"2026-07-24-ferramentas-claude-avancadas.md": ["claude", "tools", "rag"],
"2026-07-25-ferramentas-ia-open-source.md": ["ai", "tools", "open-source", "javascript", "security"],
"2026-07-25-omniroute-gateway-ia.md": ["ai", "llm", "open-source", "model-routing"],
"2026-07-26-agentes-ia-pesquisa-automacao.md": ["ai-agents", "automation", "web-scraping", "tools"],
"2026-07-26-ferramentas-plugins-skills-claude.md": ["claude", "mcp", "tools", "agent-skills"],
"2026-07-26-hermes-agente-ia-open-source.md": ["ai-agents", "tools", "open-source", "agent-memory"],
"2026-07-26-melhores-ferramentas-ia-2026.md": ["ai", "tools", "automation", "productivity"],
"2026-07-26-youtube-prompts-estrategia-canal.md": ["prompt-engineering", "content-creation", "youtube"],
"2026-07-27-ai-skills.md": ["ai-skills", "prompt-engineering", "ai-agents", "automation", "rag", "llm"],
"2026-07-27-markitdown-documentos-markdown.md": ["document-processing", "markdown", "python", "llm"],
"2026-07-27-sites-de-empregos-remotos.md": ["remote-work", "career"],
"2026-07-29-crawlee-web-scraping.md": ["web-scraping", "browser-automation", "python", "javascript", "data-engineering"],
"2026-07-29-design-md-sistemas-design-ia.md": ["design-systems", "ai-agents", "claude", "design-tokens"],
"2026-07-29-hyper-research-deep-research-agent.md": ["ai-agents", "deep-research", "open-source", "agent-memory"],
"2026-07-29-kilo-code-agentes-ia.md": ["ai-agents", "open-source", "typescript", "coding-assistants"],
"2026-07-29-kimi-k3-local.md": ["local-llm", "llm", "quantization", "hardware"],
"2026-07-29-mantis-security-review.md": ["security", "ai-agents", "code-review", "devsecops"],
"2026-07-29-open-code-review.md": ["code-review", "ai-agents", "automation", "open-source"],
"2026-07-29-openviking-context-database-ai-agents.md": ["ai-agents", "vector-database", "rag", "agent-memory"],
"2026-07-30-agentic-awesome-skills.md": ["agent-skills", "ai-agents", "prompt-engineering", "coding-assistants"],
"2026-07-30-arvore-modelos-claude.md": ["claude", "llm", "model-routing", "prompt-engineering"],
"2026-07-30-langgraph-10-motivos.md": ["ai-agents", "orchestration", "python", "workflow-engines"],
"2026-07-30-llmfit-otimizar-hardware.md": ["llm", "local-llm", "hardware", "quantization", "open-source"],
"2026-07-30-pxpipe-corte-tokens-imagens.md": ["claude", "context-engineering", "multimodal-ai", "token-optimization"],
"2026-07-30-swe-skills-bench-utilidade-real-skills-agentes.md": ["agent-skills", "ai-agents", "software-engineering", "benchmarks"],
"2026-07-30-unsloth-treinamento-local-modelos.md": ["local-llm", "llm", "fine-tuning", "open-source", "python"],
"2026-07-31-autoresearchclaw-research-autonomo.md": ["ai-agents", "deep-research", "scientific-research", "python"],
"2026-07-31-evaluations-framework.md": ["ai-evaluation", "testing", "llm", "swift"],
"2026-07-31-stallion-ota-alternativa-codepush.md": ["mobile", "react-native", "software-delivery"],
"2026-08-01-17-things-to-know-about-ai.md": ["ai", "ai-agents", "llm", "rag", "vector-database"],
"2026-08-02-dembrandt-extracao-design-systems.md": ["design-systems", "design-tokens", "web-scraping", "tools"],
"2026-08-04-candidatar-em-vagas-prompts-ats-linkedin.md": ["prompt-engineering", "career", "job-search"],
"2026-08-04-cosmo-travel-mcp.md": ["mcp", "ai-agents", "travel-tools"],
"2026-08-04-haystack-context-engineering-rag-agents.md": ["ai-agents", "rag", "context-engineering", "python"],
"2026-08-04-omnigent-meta-harness-agentes-ia.md": ["ai-agents", "orchestration", "open-source", "sandboxing"],
"2026-08-05-lark-cli-introduction.md": ["ai-agents", "automation", "cli", "agent-skills"],
"2026-08-05-memento-fine-tuning-llm-agents-without-fine-tuning-llms.md": ["ai-agents", "agent-memory", "continual-learning", "llm"],
"2026-08-05-midscene-ui-testing-por-visao.md": ["testing", "browser-automation", "computer-vision", "open-source"],
"2026-08-05-ntfy-notificacoes-http.md": ["notifications", "automation", "open-source", "http"],
"2026-08-06-archon-yaml-workflows-coding-deterministico.md": ["ai-agents", "automation", "workflow-engines", "yaml"],
"2026-08-06-codex-security.md": ["security", "ai", "code-analysis", "typescript"],
"2026-08-06-gitbutler.md": ["git", "version-control", "rust", "developer-tools"],
"2026-08-06-swift-sendable.md": ["swift", "concurrency", "thread-safety"],
"2026-08-06-uso-respeitoso-ia.md": ["ai-ethics", "collaboration", "productivity"],
"2026-08-07-livecontainer-ios-sideloading.md": ["ios", "sideloading", "mobile", "open-source"],
"2026-08-08-deerflow-super-agent-harness.md": ["ai-agents", "orchestration", "agent-memory", "open-source", "python"],
"2026-08-08-reverse-skill.md": ["agent-skills", "security", "reverse-engineering", "ai-agents"],
"2026-08-08-screensdesign-mcp.md": ["mcp", "design-systems", "mobile", "ai-agents"],
"2026-08-09-code-graph-rag.md": ["rag", "knowledge-graphs", "code-analysis", "ai-agents"],
"2026-08-09-motion-design-principles-skeletons-lazyloading.md": ["motion-design", "loading-states", "ui-ux", "web-performance"],
"2026-08-09-rxdb-banco-dados-reativo.md": ["javascript", "database", "local-first", "offline-first", "reactive-programming"],
}


def rewrite(path: Path, tags: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return
    front = match.group(1).splitlines()
    for i, line in enumerate(front):
        if line.startswith("tags:"):
            end = i + 1
            while end < len(front) and front[end].startswith((" ", "\t")) and front[end].lstrip().startswith("-"):
                end += 1
            front[i:end] = ["tags:"] + [f"  - {tag}" for tag in tags]
            break
    path.write_text("---\n" + "\n".join(front) + "\n---\n" + text[match.end():], encoding="utf-8")


def main() -> None:
    counts = Counter(tag for tags in TAGS.values() for tag in tags)
    for name, tags in TAGS.items():
        path = POSTS / name
        if path.exists():
            rewrite(path, [tag for tag in tags if counts[tag] >= 2])


if __name__ == "__main__":
    main()
