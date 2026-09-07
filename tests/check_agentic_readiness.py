#!/usr/bin/env python3
"""Verifica os sinais de prontidão agêntica do site Notes (arquivos-fonte).

Uso: python3 tests/check_agentic_readiness.py [--site-dir .]

Checa nos arquivos do repositório (sem rede):
1. 404.md existe com corpo markdown de recuperação (sitemap/llms/index).
2. index.md: H1 único como primeiro heading de conteúdo.
3. default.html: canonical, html lang, og:image, og:type, JSON-LD (Person + Organization com contactPoint/address).
4. llms.txt: seção "quando usar".
5. about.md / contact.md / privacy.md com 500+ caracteres cada.
6. sitemap.xml inclui about/contact/privacy.
7. generate-markdown-mirrors.py inclui about/contact/privacy no sitemap.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
    status = "ok" if cond else "FAIL"
    print(f"[{status}] {label}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAILURES.append(label)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.site_dir

    # 1. 404 agent-friendly
    p404 = root / "404.md"
    body404 = p404.read_text(encoding="utf-8") if p404.exists() else ""
    check("404.md existe", p404.exists())
    for needle in ("llms.txt", "index.json", "sitemap", "Todas as notas"):
        check(f"404.md menciona {needle}", needle in body404)

    # 2. H1 primeiro heading de conteúdo em index.md
    index = (root / "index.md").read_text(encoding="utf-8")
    headings = re.findall(r"<h([1-6])\b", index)
    check(
        "index.md: primeiro heading é H1",
        bool(headings) and headings[0] == "1",
        f"ordem encontrada: {headings[:4]}",
    )
    check("index.md: H1 único", headings.count("1") == 1, f"H1s: {headings.count('1')}")

    # 3. Metadados + JSON-LD no layout
    layout = (root / "_layouts" / "default.html").read_text(encoding="utf-8")
    check("layout: seo/canonical presente", "{% seo %}" in layout)
    check("layout: og:image presente", "og:image" in layout)
    # og:type é emitido pelo plugin jekyll-seo-tag ({% seo %}); basta um dos dois.
    check("layout: og:type presente (via {% seo %})", "og:type" in layout or "{% seo %}" in layout)
    check("layout: lang pt-BR", 'lang="pt-BR"' in layout or "lang='pt-BR'" in layout)
    for needle in ('"@type": "Person"', '"@type": "Organization"', '"@type": "WebSite"',
                    "contactPoint", "PostalAddress", "sameAs", '"@type": "ContactPoint"'):
        check(f"layout JSON-LD: {needle}", needle in layout)

    # 4. llms.txt com quando-usar
    llms = (root / "llms.txt").read_text(encoding="utf-8")
    check("llms.txt: seção quando-usar", "Quando usar este site" in llms)
    check("llms.txt: cita index.json e .md", "index.json" in llms and ".md" in llms)

    # 5. Trust anchors com 500+ chars
    for name in ("about.md", "contact.md", "privacy.md"):
        p = root / name
        text = ""
        if p.exists():
            raw = p.read_text(encoding="utf-8")
            text = re.sub(r"\A---\n.*?\n---\n", "", raw, flags=re.S).strip()
        check(f"{name} existe com 500+ chars", len(text) >= 500, f"len={len(text)}")

    # 6. sitemap.xml inclui trust anchors
    sitemap = (root / "sitemap.xml").read_text(encoding="utf-8")
    for needle in ("/about/", "/contact/", "/privacy/"):
        check(f"sitemap.xml inclui {needle}", needle in sitemap)

    # 7. sitemap.md gerado inclui trust anchors
    mirrors = (root / "scripts" / "generate-markdown-mirrors.py").read_text(encoding="utf-8")
    for needle in ("/about/", "/contact/", "/privacy/"):
        check(f"generate-markdown-mirrors inclui {needle}", needle in mirrors)

    print(f"\n{len(FAILURES)} falha(s)." if FAILURES else "\nTudo certo.")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
