#!/usr/bin/env python3
"""Generate the static Jekyll page that indexes post tags."""

import ast
import html
import re
import unicodedata
from collections import Counter
from pathlib import Path

POSTS_DIR = Path("_posts")
OUTPUT = Path("list-tags.md")
TAG_BASE_URL = "/notes/tag/"
MINIMUM_POSTS = 2


def parse_scalar(value: str):
    value = value.strip()
    if not value:
        return None

    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value.strip("'\"")


def parse_tags(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []

    if value.startswith("[") and value.endswith("]"):
        items = value[1:-1].split(",")
        return [item.strip().strip("'\"") for item in items if item.strip()]

    return [value.strip("'\"")]


def parse_frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Missing front matter: {path}")

    frontmatter = {}
    index = 1
    while index < len(lines) and lines[index].strip() != "---":
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
            tags = []
            index += 1
            while index < len(lines) and lines[index].startswith((" ", "\t")):
                item = lines[index].strip()
                if item.startswith("-"):
                    tags.append(item[1:].strip().strip("'\""))
                index += 1
            frontmatter[key] = tags
            continue

        frontmatter[key] = (
            parse_tags(value) if key == "tags" else parse_scalar(value)
        )
        index += 1

    if index >= len(lines):
        raise ValueError(f"Unclosed front matter: {path}")

    return frontmatter


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def collect_tag_counts() -> Counter:
    counts = Counter()
    for path in POSTS_DIR.glob("*.md"):
        tags = parse_frontmatter(path).get("tags", [])
        if not isinstance(tags, list):
            raise ValueError(f"Invalid tags in front matter: {path}")
        counts.update({str(tag).strip() for tag in tags if str(tag).strip()})
    return counts


def tag_item(tag: str, count: int) -> str:
    label = html.escape(tag)
    slug = slugify(tag)
    noun = "nota" if count == 1 else "notas"
    return "\n".join(
        [
            '      <li class="tag-index-item">',
            '        <a class="tag-index-link" '
            f'href="{TAG_BASE_URL}?tag={slug}">',
            f'          <span class="tag-index-name">#{label}</span>',
            f'          <span class="tag-index-count">{count} {noun} '
            '<span aria-hidden="true">↗</span></span>',
            "        </a>",
            "      </li>",
        ]
    )


def build_document(counts: Counter) -> str:
    tags = sorted(
        (
            tag,
            count,
        )
        for tag, count in counts.items()
        if count >= MINIMUM_POSTS
    )
    tags.sort(key=lambda item: item[0].casefold())

    items = "\n".join(tag_item(tag, count) for tag, count in tags)
    return (
        "---\n"
        "layout: page\n"
        "title: Tags\n"
        "permalink: /list-tags/\n"
        "---\n\n"
        '<section class="tag-index" aria-label="Índice de tags">\n'
        '  <div class="section-heading">\n'
        '    <p class="eyebrow">taxonomia das notas</p>\n'
        '    <p class="section-intro">Explore as notas por assunto. Cada tag abre uma página com os posts relacionados.</p>\n'
        "  </div>\n\n"
        '  <ul class="tag-grid">\n'
        f"{items}\n"
        "  </ul>\n\n"
        '  <p class="tag-index-note">Exibindo tags usadas em pelo menos duas notas.</p>\n'
        "</section>\n"
    )


def main() -> None:
    OUTPUT.write_text(build_document(collect_tag_counts()), encoding="utf-8")


if __name__ == "__main__":
    main()
