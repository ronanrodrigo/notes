#!/usr/bin/env python3
"""Normalize post tags into a shared vocabulary without damaging front matter."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

POSTS = Path(__file__).resolve().parents[1] / "_posts"
ALIASES = {
    "agents": "ai-agents", "agentes": "ai-agents", "agentes-ia": "ai-agents", "llm-agent": "ai-agents", "llm-agents": "ai-agents", "ai-agents": "ai-agents", "ai-coding": "ai-agents", "coding-agents": "ai-agents",
    "opensource": "open-source", "open-source": "open-source",
    "ferramentas": "tools", "ferramentas-ia": "tools", "tool": "tools", "tools": "tools",
    "orquestracao": "orchestration", "orchestration": "orchestration", "orchestração": "orchestration",
    "automacao": "automation", "automation": "automation", "workflow-automation": "automation",
    "ia": "ai", "llms": "llm", "modelos-llm": "llm", "llm": "llm",
    "vectordb": "vector-database", "vector-search": "vector-database", "bancos-dados-vetoriais": "vector-database",
    "localhost": "local-llm", "ia-local": "local-llm", "local-llm": "local-llm",
    "claude-code": "claude", "claude": "claude", "prompting": "prompt-engineering", "prompts": "prompt-engineering", "prompt-engineering": "prompt-engineering",
    "design-md": "design-systems", "design-tokens": "design-systems", "design-systems": "design-systems", "design": "design-systems",
    "ui-testing": "testing", "swift-testing": "testing", "testing": "testing",
    "cybersecurity": "security", "devsecops": "security", "ia-seguranca": "security", "security": "security",
    "web-scraping": "web-scraping", "browser-automation": "browser-automation",
    "agentic-skills": "agent-skills", "ai-skills": "agent-skills", "skill-library": "agent-skills", "skills": "agent-skills", "agent-skills": "agent-skills",
    "javascript": "javascript", "typescript": "typescript", "python": "python", "rust": "rust", "github": "github", "git": "git", "mobile": "mobile", "ios": "mobile", "swift": "swift", "mcp": "mcp", "rag": "rag",
}

RULES = {
    "ai-agents": ("agent", "agente", "agentic"), "rag": (" rag", "retrieval", "vector"), "open-source": ("open-source", "opensource"),
    "tools": ("ferramenta", "tool", "framework", "sdk", " cli"), "automation": ("automat", "workflow", "pipeline"),
    "design-systems": ("design", "ui", "ux", "interface"), "security": ("security", "segur", "vulnerab", "pentest"),
    "local-llm": ("local", "ollama", "inference"), "testing": ("test", "eval", "benchmark"), "mobile": ("ios", "mobile", "react-native"),
    "prompt-engineering": ("prompt", "context-engineering"), "github": ("github",), "python": ("python",), "javascript": ("javascript",), "typescript": ("typescript",), "rust": ("rust",), "swift": ("swift",), "git": ("git",), "mcp": ("mcp",),
}


def fold(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return value.strip().lower().replace(" ", "-")


def read_frontmatter(text: str) -> tuple[str, str] | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    return (match.group(1), text[match.end():]) if match else None


def parse_tags(frontmatter: str) -> list[str]:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("tags:"):
            continue
        value = line[len("tags:"):].strip()
        if value.startswith("[") and value.endswith("]"):
            return [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
        result: list[str] = []
        for child in lines[index + 1:]:
            if child.startswith((" ", "\t")) and child.lstrip().startswith("-"):
                result.append(child.lstrip()[1:].strip().strip("'\""))
            else:
                break
        return result
    return []


def normalize(tag: str) -> str:
    value = fold(tag)
    return ALIASES.get(value, value)


def replace_tags(frontmatter: str, tags: list[str]) -> str:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("tags:"):
            continue
        end = index + 1
        while end < len(lines) and lines[end].startswith((" ", "\t")) and lines[end].lstrip().startswith("-"):
            end += 1
        lines[index:end] = ["tags:"] + [f"  - {tag}" for tag in tags]
        return "\n".join(lines)
    return frontmatter + "\ntags:\n" + "\n".join(f"  - {tag}" for tag in tags)


def main() -> None:
    data: dict[Path, list[str]] = {}
    for path in sorted(POSTS.glob("*.md")):
        parsed = read_frontmatter(path.read_text(encoding="utf-8"))
        if not parsed:
            continue
        frontmatter, body = parsed
        tags = [normalize(tag) for tag in parse_tags(frontmatter)]
        haystack = fold(path.stem + " " + body)
        tags += [tag for tag, needles in RULES.items() if any(needle in haystack for needle in needles)]
        data[path] = list(dict.fromkeys(tags))

    counts = Counter(tag for tags in data.values() for tag in tags)
    for path, tags in data.items():
        shared = [tag for tag in tags if counts[tag] >= 2]
        if not shared:
            shared = ["ai"]
        text = path.read_text(encoding="utf-8")
        parsed = read_frontmatter(text)
        if parsed:
            frontmatter, body = parsed
            path.write_text("---\n" + replace_tags(frontmatter, shared) + "\n---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    main()
