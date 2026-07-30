#!/usr/bin/env python3
"""Generate a small, deterministic JSON index for the Jekyll posts."""

import ast
import json
import re
from pathlib import Path

POSTS_DIR = Path("_posts")
OUTPUT = Path("index.json")


def parse_scalar(value: str):
    value = value.strip()
    if not value:
        return None

    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value


def parse_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\\A---\\s*\\n(.*?)\\n---(?:\\s*\\n|\\Z)", content, re.DOTALL)
    if not match:
        raise ValueError(f"Missing front matter: {path}")

    frontmatter = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            continue
        frontmatter[key.strip()] = parse_scalar(value)

    return frontmatter


def post_metadata(path: Path) -> dict:
    match = re.match(r"(\\d{4}-\\d{2}-\\d{2})-(.+)\\.md$", path.name)
    if not match:
        raise ValueError(f"Invalid post filename: {path}")

    filename_date, slug = match.groups()
    frontmatter = parse_frontmatter(path)
    tags = frontmatter.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        raise ValueError(f"Invalid tags in front matter: {path}")

    return {
        "date": str(frontmatter.get("date", filename_date)),
        "slug": slug,
        "path": path.as_posix(),
        "tags": tags,
        "description": frontmatter.get("description"),
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
