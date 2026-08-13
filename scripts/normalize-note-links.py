#!/usr/bin/env python3
"""Convert plain URLs in legacy notes to clickable Markdown links."""

from pathlib import Path
import re
import sys


ROOT = Path("_notes")
URL = re.compile(r"https?://[^\s<>\[\]`]+")
LINK = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
FENCE = re.compile(r"```.*?```", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
HEADING = re.compile(r"(?m)^\s{0,3}#{1,6}[^\n]*$")


def protected_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for pattern in (FENCE, COMMENT, FRONTMATTER, LINK, HEADING):
        spans.extend((match.start(), match.end()) for match in pattern.finditer(text))
    spans.extend((match.start(), match.end()) for match in re.finditer(r"(`+)(.*?)\1", text, re.S))
    spans.sort()

    merged: list[tuple[int, int]] = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def is_protected(position: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= position < end for start, end in spans)


def normalize(text: str) -> tuple[str, int]:
    spans = protected_spans(text)
    output: list[str] = []
    last = 0
    converted = 0

    for match in URL.finditer(text):
        if is_protected(match.start(), spans):
            continue

        raw = match.group(0)
        trailing = ""
        while raw and raw[-1] in ".,;:!?":
            trailing = raw[-1] + trailing
            raw = raw[:-1]
        if not raw:
            continue

        output.append(text[last : match.start()])
        url = raw.replace("\\/", "/")
        output.append(f"[Acesse aqui]({url})")
        output.append(trailing)
        last = match.end()
        converted += 1

    output.append(text[last:])
    return "".join(output), converted


def validate(path: Path, text: str) -> list[str]:
    errors = []
    spans = protected_spans(text)
    for match in URL.finditer(text):
        if not is_protected(match.start(), spans):
            errors.append(f"{path}: plain URL at offset {match.start()}: {match.group(0)}")
    for match in re.finditer(r"\[Acesse aqui\]\((.*?)\)", text):
        if not re.fullmatch(r"https?://[^\s<>]+", match.group(1)):
            errors.append(f"{path}: malformed Acesse aqui link: {match.group(0)}")
    if re.search(r"\[Acesse aqui\]\(\s*\[Acesse aqui\]", text):
        errors.append(f"{path}: duplicated nested Acesse aqui link")
    return errors


def main() -> int:
    files = sorted(ROOT.rglob("*.md")) if ROOT.exists() else []
    changed = []
    converted = 0

    for path in files:
        original = path.read_text(encoding="utf-8")
        updated, count = normalize(original)
        converted += count
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path))

    errors = []
    for path in files:
        errors.extend(validate(path, path.read_text(encoding="utf-8")))

    print(f"Arquivos analisados: {len(files)}")
    print(f"Arquivos alterados: {len(changed)}")
    print(f"URLs convertidas: {converted}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Validação concluída: nenhuma URL pura, duplicação ou link malformado encontrado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
