#!/usr/bin/env bash

set -euo pipefail

expected_branch="migrate/notes-to-jekyll-posts"
current_branch="$(git branch --show-current)"

if [[ "$current_branch" != "$expected_branch" ]]; then
  echo "Refusing to run outside $expected_branch (current branch: $current_branch)." >&2
  exit 1
fi

shopt -s nullglob
notes=( _notes/*.md )

if (( ${#notes[@]} == 0 )); then
  echo "No Markdown files found in _notes/."
  exit 0
fi

mkdir -p _posts

for source in "${notes[@]}"; do
  filename="$(basename "$source")"

  if [[ ! "$filename" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-.+\.md$ ]]; then
    echo "Invalid Jekyll post filename: $source" >&2
    exit 1
  fi

  destination="_posts/$filename"
  temporary="_posts/.migrating-$filename"

  if [[ -e "$destination" ]]; then
    if ! cmp -s "$source" "$destination"; then
      echo "Content mismatch between $source and $destination." >&2
      exit 1
    fi

    # Move through a temporary path so Git records the operation as a
    # rename instead of leaving duplicate source and destination files.
    git mv "$destination" "$temporary"
    git mv "$source" "$destination"
    rm "$temporary"
  else
    git mv "$source" "$destination"
  fi

done

if [[ -d _notes ]] && [[ -z "$(find _notes -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  rmdir _notes
fi

echo "Moved ${#notes[@]} Markdown file(s) from _notes/ to _posts/."
