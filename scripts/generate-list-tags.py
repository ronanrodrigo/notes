#!/usr/bin/env python3
"""Generate a JSON index of tags used by Jekyll posts."""

import ast
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

POSTS_DIR = Path("_posts")
OUTPUT = Path("list-tags.json")
TAG_BASE_URL = "https://ronanrodrigo.dev/notes/tag/"
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

        frontmatter[key] = parse_tags(value) if key == "tags" else parse_scalar(value)
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


def build_document(counts: Counter) -> list[dict]:
    tags = [
        {
            "tag": tag,
            "url": f"{TAG_BASE_URL}?tag={slugify(tag)}",
        }
        for tag, count in counts.items()
        if count >= MINIMUM_POSTS
    ]
    return sorted(tags, key=lambda item: item["tag"].casefold())


def main() -> None:
    OUTPUT.write_text(
        json.dumps(build_document(collect_tag_counts()), ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
