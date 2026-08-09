#!/usr/bin/env python3
"""Normalize tags while preserving every YAML front-matter field."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

POSTS = Path(__file__).resolve().parents[1] / "_posts"
ALIASES = {
    "agents": "ai-agents", "agentes": "ai-agents", "agentes-ia": "ai-agents", "llm-agent": "ai-agents", "llm-agents": "ai-agents", "ai-agents": "ai-agents", "ai-coding": "ai-agents", "coding-agents": "ai-agents",
    "opensource": "open-source", "open-source": "open-source", "ferramentas": "tools", "ferramentas-ia": "tools", "tool": "tools", "tools": "tools",
    "orquestracao": "orchestration", "orchestração": "orchestration", "orchestration": "orchestration", "automacao": "automation", "automation": "automation", "workflow-automation": "automation",
    "ia": "ai", "llms": "llm", "modelos-llm": "llm", "llm": "llm", "vectordb": "vector-database", "vector-search": "vector-database", "bancos-dados-vetoriais": "vector-database",
    "localhost": "local-llm", "ia-local": "local-llm", "local-llm": "local-llm", "claude-code": "claude", "claude": "claude", "prompting": "prompt-engineering", "prompts": "prompt-engineering", "prompt-engineering": "prompt-engineering",
    "design-md": "design-systems", "design-tokens": "design-systems", "design-systems": "design-systems", "design": "design-systems", "ui-testing": "testing", "swift-testing": "testing", "testing": "testing",
    "cybersecurity": "security", "devsecops": "security", "ia-seguranca": "security", "security": "security", "web-scraping": "web-scraping", "browser-automation": "browser-automation",
    "agentic-skills": "agent-skills", "ai-skills": "agent-skills", "skill-library": "agent-skills", "skills": "agent-skills", "agent-skills": "agent-skills", "javascript": "javascript", "typescript": "typescript", "python": "python", "rust": "rust", "github": "github", "git": "git", "mobile": "mobile", "ios": "mobile", "swift": "swift", "mcp": "mcp", "rag": "rag",
}
RULES = {"ai-agents": ("agent", "agente", "agentic"), "rag": ("rag", "retrieval", "vector"), "open-source": ("open-source", "opensource"), "tools": ("ferramenta", "tool", "framework", "sdk", " cli"), "automation": ("automat", "workflow", "pipeline"), "design-systems": ("design", "ui", "ux", "interface"), "security": ("security", "segur", "vulnerab", "pentest"), "local-llm": ("local", "ollama", "inference"), "testing": ("test", "eval", "benchmark"), "mobile": ("ios", "mobile", "react-native"), "prompt-engineering": ("prompt", "context-engineering"), "github": ("github",), "python": ("python",), "javascript": ("javascript",), "typescript": ("typescript",), "rust": ("rust",), "swift": ("swift",), "git": ("git",), "mcp": ("mcp",)}


def fold(value: str) -> str:
    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().strip().lower().replace(" ", "-")


def parse_frontmatter(text: str) -> tuple[list[str], str] | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    return (match.group(1).splitlines(), text[match.end():]) if match else None


def parse_tags(lines: list[str]) -> list[str]:
    for i, line in enumerate(lines):
        if not line.startswith("tags:"):
            continue
        value = line[5:].strip()
        if value.startswith("[") and value.endswith("]"):
            return [x.strip().strip("'\"") for x in value[1:-1].split(",") if x.strip()]
        result = []
        for child in lines[i + 1:]:
            if child.startswith((" ", "\t")) and child.lstrip().startswith("-"):
                result.append(child.lstrip()[1:].strip().strip("'\""))
            else:
                break
        return result
    return []


def replace_tags(lines: list[str], tags: list[str]) -> list[str]:
    for i, line in enumerate(lines):
        if not line.startswith("tags:"):
            continue
        end = i + 1
        while end < len(lines) and lines[end].startswith((" ", "\t")) and lines[end].lstrip().startswith("-"):
            end += 1
        lines[i:end] = ["tags:"] + [f"  - {tag}" for tag in tags]
        return lines
    return lines + ["tags:"] + [f"  - {tag}" for tag in tags]


def main() -> None:
    data = {}
    for path in sorted(POSTS.glob("*.md")):
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not parsed:
            continue
        lines, body = parsed
        tags = [ALIASES.get(fold(tag), fold(tag)) for tag in parse_tags(lines)]
        haystack = fold(path.stem + " " + body)
        tags += [tag for tag, needles in RULES.items() if any(needle in haystack for needle in needles)]
        data[path] = list(dict.fromkeys(tags))
    counts = Counter(tag for tags in data.values() for tag in tags)
    for path, tags in data.items():
        shared = [tag for tag in tags if counts[tag] >= 2] or ["ai"]
        text = path.read_text(encoding="utf-8")
        parsed = parse_frontmatter(text)
        if parsed:
            lines, body = parsed
            path.write_text("---\n" + "\n".join(replace_tags(lines, shared)) + "\n---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    main()
