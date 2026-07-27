#!/usr/bin/env bash

set -euo pipefail

expected_branch="migrate/notes-to-jekyll-posts"
current_ref="${GITHUB_REF:-}"

if [[ "$current_ref" != "refs/heads/$expected_branch" ]]; then
  echo "Refusing to run outside $expected_branch (GITHUB_REF: ${current_ref:-unset})." >&2
  exit 1
fi

shopt -s nullglob
notes=( _notes/*.md )

if (( ${#notes[@]} == 0 )); then
  echo "No Markdown files found in _notes/."
  exit 0
fi

for source in "${notes[@]}"; do
  filename="$(basename "$source")"
  destination="_posts/$filename"

  if [[ ! "$filename" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-.+\.md$ ]]; then
    echo "Invalid Jekyll post filename: $source" >&2
    exit 1
  fi

  if [[ ! -f "$destination" ]]; then
    echo "Expected post is missing: $destination" >&2
    exit 1
  fi

  if ! cmp -s "$source" "$destination"; then
    echo "Content mismatch between $source and $destination." >&2
    exit 1
  fi
done

for source in "${notes[@]}"; do
  rm "$source"
done

if [[ -d _notes ]] && [[ -z "$(find _notes -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  rmdir _notes
fi

echo "Validated and removed ${#notes[@]} duplicated Markdown file(s) from _notes/."
