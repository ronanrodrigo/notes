#!/usr/bin/env python3
"""Remove eligible Markdown H1 headings from legacy notes and validate them."""

from pathlib import Path
import difflib
import re
import sys


ROOT = Path("_notes")
H1 = re.compile(r"^[ \t]{0,3}#(?!#)[ \t]+.+$")
H2_OR_LOWER = re.compile(r"^[ \t]{0,3}#{2,}[ \t]+.+$")


def protected_lines(lines: list[str]) -> set[int]:
    protected = set()
    fenced = False
    html_comment = False
    frontmatter = bool(lines and lines[0].rstrip("\r\n") == "---")

    for index, line in enumerate(lines):
        stripped = line.rstrip("\r\n")
        if frontmatter:
            protected.add(index)
            if index > 0 and stripped == "---":
                frontmatter = False
            continue
        if html_comment:
            protected.add(index)
            if "-->" in line:
                html_comment = False
            continue
        if "<!--" in line:
            protected.add(index)
            if "-->" not in line[line.index("<!--") + 4 :]:
                html_comment = True
            continue
        if re.match(r"^[ \t]{0,3}```", line):
            protected.add(index)
            fenced = not fenced
            continue
        if fenced:
            protected.add(index)
    return protected


def main() -> int:
    files = sorted(ROOT.rglob("*.md")) if ROOT.exists() else []
    changed = []
    removed_count = 0
    originals = {}

    for path in files:
        original = path.read_text(encoding="utf-8")
        originals[path] = original
        lines = original.splitlines(keepends=True)
        protected = protected_lines(lines)
        kept = []
        count = 0

        for index, line in enumerate(lines):
            if index not in protected and H1.match(line):
                count += 1
            else:
                kept.append(line)

        updated = "".join(kept)
        if count and updated != original:
            if lines and lines[0].rstrip("\r\n") == "---":
                updated = re.sub(
                    r"(^---\r?\n.*?^---[ \t]*\r?\n)(?:[ \t]*\r?\n){3,}",
                    r"\1\n\n",
                    updated,
                    count=1,
                    flags=re.MULTILINE | re.DOTALL,
                )
            path.write_text(updated, encoding="utf-8")
            changed.append(path)
            removed_count += count

    failures = []
    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        protected = protected_lines(lines)
        remaining = [
            (index + 1, line.rstrip("\r\n"))
            for index, line in enumerate(lines)
            if index not in protected and H1.match(line)
        ]
        if remaining:
            failures.append(f"{path}: H1 real restante em {remaining}")

    for path in changed:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        if lines and lines[0].rstrip("\r\n") == "---":
            if not any(re.match(r"^title[ \t]*:", line) for line in lines[1:]):
                failures.append(f"{path}: campo title ausente após alteração")

    for path in changed:
        removed_lines = [
            line[2:]
            for line in difflib.ndiff(
                originals[path].splitlines(), path.read_text(encoding="utf-8").splitlines()
            )
            if line.startswith("- ")
        ]
        for line in removed_lines:
            if H2_OR_LOWER.match(line):
                failures.append(f"{path}: H2/H3 removido indevidamente: {line}")

    print(f"Arquivos analisados: {len(files)}")
    print(f"Arquivos alterados: {len(changed)}")
    print(f"H1 removidos: {removed_count}")
    if failures:
        print("\n".join(failures))
        print("VALIDAÇÃO: FALHOU")
        return 1
    print("VALIDAÇÃO: APROVADA — nenhum H1 real elegível permaneceu; H2/H3 e frontmatter preservados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
