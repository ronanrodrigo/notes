#!/usr/bin/env bash

set -euo pipefail

# The workflow is dispatched from main and checks out this migration branch.
# The source files in _notes are authoritative: copy them byte-for-byte to
# _posts before removing the duplicated source files.

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
done

for source in "${notes[@]}"; do
  filename="$(basename "$source")"
  destination="_posts/$filename"
  temporary="_posts/.migrating-$filename"

  # Preserve the authoritative note exactly, including frontmatter types,
  # blank lines, line endings as read by the runner, and Markdown content.
  cp "$source" "$temporary"
  mv "$temporary" "$destination"
  rm "$source"
done

if [[ -d _notes ]] && [[ -z "$(find _notes -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  rmdir _notes
fi

echo "Preserved and cleaned ${#notes[@]} Markdown file(s); _notes is no longer used."
