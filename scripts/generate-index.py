#!/usr/bin/env python3
"""Generate a deterministic JSON index for the Jekyll posts."""

import ast
import json
import re
from pathlib import Path

POSTS_DIR = Path("_posts")
OUTPUT = Path("index.json")
BASE_URL = "https://ronanrodrigo.dev/notes"
AUTHOR = {
    "name": "Ronan Rodrigo Nunes",
    "url": "https://ronanrodrigo.dev/",
}


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


def dated_url(date: str, slug: str) -> str:
    match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", date)
    if not match:
        raise ValueError(f"Invalid post date for {slug}: {date}")
    year, month, day = match.groups()
    return f"{BASE_URL}/{year}/{month}/{day}/{slug}/"


def post_metadata(path: Path) -> dict:
    match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", path.name)
    if not match:
        raise ValueError(f"Invalid post filename: {path}")

    filename_date, slug = match.groups()
    frontmatter = parse_frontmatter(path)
    tags = frontmatter.get("tags", [])
    if not isinstance(tags, list):
        raise ValueError(f"Invalid tags in front matter: {path}")

    date = str(frontmatter.get("date", filename_date))
    return {
        "title": frontmatter.get("title") or slug.replace("-", " ").title(),
        "date": date,
        "published": date,
        "modified": frontmatter.get("modified", date),
        "slug": slug,
        "url": dated_url(date, slug),
        "markdown_url": f"{BASE_URL}/{slug}.md",
        "path": path.as_posix(),
        "tags": tags,
        "description": frontmatter.get("description"),
        "author": AUTHOR,
        "status": "published",
    }


def main() -> None:
    posts = [post_metadata(path) for path in POSTS_DIR.glob("*.md")]
    posts.sort(key=lambda post: (post["date"], post["slug"]), reverse=True)

    OUTPUT.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
