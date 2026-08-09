#!/usr/bin/env python3
"""Normalize post tags, reuse a shared vocabulary, and remove singleton tags."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

POSTS = Path(__file__).resolve().parents[1] / "_posts"

ALIASES = {
    "opensource": "open-source",
    "open-source": "open-source",
    "agents": "ai-agents",
    "agentic-agents": "ai-agents",
    "llm-agent": "ai-agents",
    "llm-agents": "ai-agents",
    "ai-agents": "ai-agents",
    "ia-agentes": "ai-agents",
    "ia": "ai",
    "ferramentas-ia": "tools",
    "ferramentas": "tools",
    "tool": "tools",
    "tools": "tools",
    "orchestração": "orchestration",
    "orquestracao": "orchestration",
    "orchestration": "orchestration",
    "automation": "automation",
    "automacao": "automation",
    "rag": "rag",
    "vectordb": "vector-database",
    "bancos-dados-vetoriais": "vector-database",
    "vector-search": "vector-database",
    "localhost": "local-llm",
    "ia-local": "local-llm",
    "local-llm": "local-llm",
    "llm": "llm",
    "llms": "llm",
    "modelos-llm": "llm",
    "github": "github",
    "claude-code": "claude",
    "prompting": "prompt-engineering",
    "prompts": "prompt-engineering",
    "python": "python",
    "javascript": "javascript",
    "typescript": "typescript",
    "rust": "rust",
    "design-md": "design-systems",
    "design-tokens": "design-systems",
    "design": "design",
    "code-review": "code-review",
    "security": "security",
    "cybersecurity": "security",
    "devsecops": "security",
    "ia-seguranca": "security",
    "web-scraping": "web-scraping",
    "browser-automation": "browser-automation",
    "mobile": "mobile",
    "ios": "ios",
    "swift": "swift",
    "git": "git",
    "testing": "testing",
    "ui-testing": "testing",
    "skills": "agent-skills",
    "agent-skills": "agent-skills",
}

# Tags intentionally retained as part of the shared vocabulary. Every tag that
# remains in the generated site must occur on at least two posts.
SHARED = {
    "ai", "ai-agents", "agent-skills", "automation", "browser-automation",
    "claude", "code-review", "design", "design-systems", "git", "github",
    "javascript", "llm", "local-llm", "mcp", "mobile", "open-source",
    "orchestration", "prompt-engineering", "python", "rag", "rust", "security",
    "swift", "testing", "tools", "typescript", "vector-database", "web-scraping",
}


def parse_tags(frontmatter: str) -> list[str]:
    inline = re.search(r"^tags:\s*\[([^]]*)\]\s*$", frontmatter, re.MULTILINE)
    if inline:
        return [x.strip().strip("'\"") for x in inline.group(1).split(",") if x.strip()]
    block = re.search(r"^tags:\s*$\n((?:^[ \t]+-[^\n]*\n?)*)", frontmatter, re.MULTILINE)
    if not block:
        return []
    return [re.sub(r"^\s*-\s*", "", line).strip().strip("'\"") for line in block.group(1).splitlines()]


def normalize(tag: str) -> str:
    tag = tag.strip().lower().replace(" ", "-")
    return ALIASES.get(tag, tag)


def rewrite(path: Path, tags: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return
    frontmatter = match.group(1)
    replacement = "tags:\n" + "".join(f"  - {tag}\n" for tag in tags)
    updated = re.sub(r"^tags:\s*(?:\[[^\n]*\]|\n(?:^[ \t]+-[^\n]*\n?)*)", replacement.rstrip("\n"), frontmatter, count=1, flags=re.MULTILINE)
    if updated == frontmatter:
        updated = frontmatter.rstrip() + "\n" + replacement.rstrip("\n")
    path.write_text("---\n" + updated.rstrip() + "\n---\n" + text[match.end():], encoding="utf-8")


def main() -> None:
    posts = sorted(POSTS.glob("*.md"))
    data: dict[Path, list[str]] = {}
    for path in posts:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            continue
        tags = list(dict.fromkeys(normalize(t) for t in parse_tags(match.group(1))))
        # Keep only tags from the shared vocabulary; this is the deliberate
        # refactoring point that makes semantically equivalent tags converge.
        data[path] = [t for t in tags if t in SHARED]

    counts = Counter(tag for tags in data.values() for tag in tags)
    for path, tags in data.items():
        kept = [tag for tag in tags if counts[tag] >= 2]
        rewrite(path, kept)


if __name__ == "__main__":
    main()
