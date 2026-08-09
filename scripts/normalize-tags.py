#!/usr/bin/env python3
"""Normalize Jekyll post tags into a small, reusable taxonomy.

The source tags are intentionally not kept as-is: aliases and one-off labels are
mapped to broader concepts, and the final pass removes any label used by fewer
than two posts. Every post receives at least one shared topic label.
"""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

POSTS = Path(__file__).resolve().parents[1] / "_posts"

ALIASES = {
    "agents": "ai-agents", "agentes": "ai-agents", "agentes-ia": "ai-agents",
    "llm-agent": "ai-agents", "llm-agents": "ai-agents", "ai-agents": "ai-agents",
    "agentic-agents": "ai-agents", "ai-coding": "ai-agents", "coding-agents": "ai-agents",
    "opensource": "open-source", "open-source": "open-source",
    "ferramentas": "tools", "ferramentas-ia": "tools", "tool": "tools", "tools": "tools",
    "orquestracao": "orchestration", "orchestration": "orchestration", "orchestração": "orchestration",
    "automacao": "automation", "automation": "automation", "workflow-automation": "automation",
    "ia": "ai", "llms": "llm", "modelos-llm": "llm", "llm": "llm",
    "vectordb": "vector-database", "vector-search": "vector-database", "bancos-dados-vetoriais": "vector-database",
    "localhost": "local-llm", "ia-local": "local-llm", "local-llm": "local-llm",
    "claude-code": "claude", "claude": "claude",
    "prompting": "prompt-engineering", "prompts": "prompt-engineering", "prompt-engineering": "prompt-engineering",
    "design-md": "design-systems", "design-tokens": "design-systems", "design-systems": "design-systems",
    "ui-testing": "testing", "swift-testing": "testing", "testing": "testing",
    "cybersecurity": "security", "devsecops": "security", "ia-seguranca": "security", "security": "security",
    "web-scraping": "web-scraping", "browser-automation": "browser-automation",
    "agentic-skills": "agent-skills", "ai-skills": "agent-skills", "skill-library": "agent-skills", "skills": "agent-skills",
    "javascript": "javascript", "typescript": "typescript", "python": "python", "rust": "rust",
    "github": "github", "git": "git", "mobile": "mobile", "ios": "ios", "swift": "swift", "mcp": "mcp", "rag": "rag",
}

FALLBACKS = {
    "ai-agents", "ai", "agent-skills", "automation", "claude", "design-systems",
    "github", "javascript", "llm", "local-llm", "mcp", "mobile", "open-source",
    "orchestration", "prompt-engineering", "python", "rag", "rust", "security",
    "swift", "testing", "tools", "typescript", "vector-database", "web-scraping",
}


def fold(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return value.strip().lower().replace(" ", "-")


def parse_tags(frontmatter: str) -> list[str]:
    inline = re.search(r"^tags:\s*\[([^]]*)\]\s*$", frontmatter, re.MULTILINE)
    if inline:
        return [x.strip().strip("'\"") for x in inline.group(1).split(",") if x.strip()]
    block = re.search(r"^tags:\s*$\n((?:^[ \t]+-[^\n]*\n?)*)", frontmatter, re.MULTILINE)
    if not block:
        return []
    return [re.sub(r"^\s*-\s*", "", line).strip().strip("'\"") for line in block.group(1).splitlines()]


def normalize(tag: str) -> str:
    value = fold(tag)
    return ALIASES.get(value, value)


def inferred_tags(path: Path, text: str, existing: list[str]) -> list[str]:
    haystack = fold(path.stem + " " + text)
    result = list(existing)
    rules = [
        ("ai-agents", ("agent", "agente", "agentic")),
        ("rag", (" rag ", "retrieval", "vector")),
        ("open-source", ("open-source", "opensource")),
        ("tools", ("ferramenta", "tool", "framework", "sdk", "cli")),
        ("automation", ("automat", "workflow", "pipeline")),
        ("design-systems", ("design", "ui", "ux", "interface")),
        ("security", ("security", "segur", "vulnerab", "pentest")),
        ("local-llm", ("local", "ollama", "inference")),
        ("testing", ("test", "eval", "benchmark")),
        ("mobile", ("ios", "mobile", "react-native")),
        ("prompt-engineering", ("prompt", "context-engineering")),
        ("github", ("github", "git ")),
    ]
    for tag, needles in rules:
        if any(needle in haystack for needle in needles):
            result.append(tag)
    return list(dict.fromkeys(tag for tag in result if tag in FALLBACKS))


def rewrite(path: Path, tags: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return
    frontmatter = match.group(1)
    replacement = "tags:\n" + "".join(f"  - {tag}\n" for tag in tags)
    updated = re.sub(
        r"^tags:\s*(?:\[[^\n]*\]|\n(?:^[ \t]+-[^\n]*\n?)*)",
        replacement.rstrip("\n"), frontmatter, count=1, flags=re.MULTILINE,
    )
    if updated == frontmatter:
        updated = frontmatter.rstrip() + "\n" + replacement.rstrip("\n")
    path.write_text("---\n" + updated.rstrip() + "\n---\n" + text[match.end():], encoding="utf-8")


def main() -> None:
    data: dict[Path, list[str]] = {}
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if match:
            original = list(dict.fromkeys(normalize(tag) for tag in parse_tags(match.group(1))))
            data[path] = inferred_tags(path, text, original)

    counts = Counter(tag for tags in data.values() for tag in tags)
    for path, tags in data.items():
        # The second pass is deliberately global: singleton labels disappear
        # even when they were present in the original front matter.
        shared = [tag for tag in tags if counts[tag] >= 2]
        if not shared:
            shared = ["ai"] if "ai" in fold(path.stem + " " + path.read_text(encoding="utf-8")) else ["tools"]
        rewrite(path, shared)


if __name__ == "__main__":
    main()
