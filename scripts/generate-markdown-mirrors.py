#!/usr/bin/env python3
"""Generate clean Markdown mirrors and a Markdown sitemap for the public site."""

from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

BASE_URL = "https://ronanrodrigo.dev/notes"
POSTS_DIR = Path("_posts")


def scalar(value: str) -> str | None:
    value = value.strip()
    if not value:
        return None
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError):
        parsed = value.strip("'\"")
    return str(parsed) if parsed is not None else None


def frontmatter(path: Path) -> tuple[dict[str, str | list[str]], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"Missing or invalid front matter: {path}")

    values: dict[str, str | list[str]] = {}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        key, separator, value = line.partition(":")
        if not separator:
            index += 1
            continue
        key = key.strip()
        if key == "tags" and not value.strip():
            tags: list[str] = []
            index += 1
            while index < len(lines) and lines[index].startswith((" ", "\t")):
                item = lines[index].strip()
                if item.startswith("-"):
                    tags.append(item[1:].strip().strip("'\""))
                index += 1
            values[key] = tags
            continue
        values[key] = scalar(value) or ""
        index += 1

    return values, match.group(2).lstrip()


def dated_url(date: str, slug: str) -> str:
    match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", date)
    if not match:
        raise ValueError(f"Invalid post date for {slug}: {date}")
    year, month, day = match.groups()
    return f"{BASE_URL}/{year}/{month}/{day}/{slug}/"


def post_metadata(path: Path) -> tuple[str, dict[str, str | list[str]], str]:
    match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", path.name)
    if not match:
        raise ValueError(f"Invalid post filename: {path}")
    filename_date, slug = match.groups()
    metadata, body = frontmatter(path)
    metadata.setdefault("date", filename_date)
    metadata.setdefault("title", slug.replace("-", " ").title())
    return slug, metadata, body


def render_mirror(slug: str, metadata: dict[str, str | list[str]], body: str) -> str:
    title = str(metadata["title"])
    date = str(metadata["date"])
    description = str(metadata.get("description", ""))
    tags = metadata.get("tags", [])
    tags_text = ", ".join(str(tag) for tag in tags) if isinstance(tags, list) else str(tags)

    header = [f"# {title}", "", f"- Publicado: {date}"]
    if description:
        header.append(f"- Resumo: {description}")
    if tags_text:
        header.append(f"- Tags: {tags_text}")
    header.extend(
        [
            f"- Página HTML: {dated_url(date, slug)}",
            "",
            "---",
            "",
        ]
    )
    return "\n".join(header) + body.rstrip() + "\n"


def render_sitemap(posts: list[tuple[str, dict[str, str | list[str]], str]]) -> str:
    lines = [
        "# Mapa do site",
        "",
        "> Índice Markdown dos recursos públicos do Notes. Use o sitemap XML para a descoberta completa das URLs.",
        "",
        "## Recursos de navegação",
        "",
        f"- [Todas as notas]({BASE_URL}/): índice cronológico das notas.",
        f"- [Guia para agentes]({BASE_URL}/agent/): escopo, regras e fluxo de navegação.",
        f"- [Índice JSON]({BASE_URL}/index.json): metadados estruturados das notas.",
        f"- [Índice llms.txt]({BASE_URL}/llms.txt): mapa compacto para agentes.",
        f"- [Lista de tags]({BASE_URL}/list-tags/): tags reutilizadas no conteúdo.",
        f"- [Tags e posts]({BASE_URL}/tags/): índice agrupado por assunto.",
        f"- [Feed]({BASE_URL}/feed.xml): publicações recentes.",
        f"- [Sitemap XML]({BASE_URL}/sitemap.xml): URLs públicas em XML.",
        "",
        "## Notas",
        "",
    ]
    for slug, metadata, _ in posts:
        title = str(metadata["title"])
        description = str(metadata.get("description", "")).strip()
        suffix = f": {description}" if description else ""
        lines.append(f"- [{title}]({BASE_URL}/{slug}.md){suffix}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    posts = [post_metadata(path) for path in POSTS_DIR.glob("*.md")]
    posts.sort(key=lambda item: (str(item[1].get("date", "")), item[0]), reverse=True)
    args.output.mkdir(parents=True, exist_ok=True)

    for slug, metadata, body in posts:
        (args.output / f"{slug}.md").write_text(
            render_mirror(slug, metadata, body), encoding="utf-8"
        )

    (args.output / "sitemap.md").write_text(
        render_sitemap(posts), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
