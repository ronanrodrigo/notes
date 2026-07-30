#!/usr/bin/env python3
"""Generate a small, deterministic JSON index for the Jekyll posts."""

import json
import re
from datetime import date
from pathlib import Path

POSTS_DIR = Path("_posts")
OUTPUT = Path("index.json")


def post_metadata(path: Path) -> dict[str, str]:
    match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", path.name)
    if not match:
        raise ValueError(f"Invalid post filename: {path}")

    post_date, slug = match.groups()
    return {
        "date": post_date,
        "slug": slug,
        "path": path.as_posix(),
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
