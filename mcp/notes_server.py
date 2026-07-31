"""MCP server for searching and reusing the notes repository."""

from __future__ import annotations

import json
import os
import re
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import PurePosixPath
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from mcp.server.fastmcp import FastMCP


OWNER = os.getenv("NOTES_GITHUB_OWNER", "ronanrodrigo")
REPO = os.getenv("NOTES_GITHUB_REPO", "notes")
REF = os.getenv("NOTES_GITHUB_REF", "main")
API_ROOT = f"https://api.github.com/repos/{OWNER}/{REPO}"
RAW_ROOT = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{REF}"

mcp = FastMCP("ronanrodrigo-notes")


def _get(url: str) -> Any:
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "notes-mcp"})
    token = os.getenv("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(request, timeout=20) as response:
            payload = response.read().decode("utf-8")
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"Falha ao consultar o GitHub: {exc}") from exc
    return json.loads(payload)


@lru_cache(maxsize=1)
def _index() -> list[dict[str, Any]]:
    data = _get(f"{RAW_ROOT}/index.json")
    if not isinstance(data, list):
        raise RuntimeError("index.json não contém uma lista de notas")
    return data


def _normalize(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"[^\w\s-]", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def _score(query: str, note: dict[str, Any], content: str = "") -> float:
    query = _normalize(query)
    if not query:
        return 0.0
    fields = {
        "slug": _normalize(str(note.get("slug", ""))),
        "tags": _normalize(" ".join(note.get("tags", []))),
        "description": _normalize(str(note.get("description", ""))),
        "content": _normalize(content),
    }
    query_tokens = query.split()
    token_hits = sum(any(token in field for field in fields.values()) for token in query_tokens)
    token_score = token_hits / len(query_tokens)
    exact_score = max(SequenceMatcher(None, query, field).ratio() for field in fields.values())
    tag_score = max((SequenceMatcher(None, query, _normalize(tag)).ratio() for tag in note.get("tags", [])), default=0.0)
    return round((token_score * 0.45) + (exact_score * 0.35) + (tag_score * 0.20), 4)


def _validate_path(path: str) -> str:
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or ".." in candidate.parts or not str(candidate).startswith("_posts/"):
        raise ValueError("path deve apontar para um arquivo dentro de _posts/")
    return str(candidate)


@mcp.tool()
def search_notes(query: str, tags: list[str] | None = None, limit: int = 10, include_content: bool = False) -> dict[str, Any]:
    """Busca notas por texto, slug, descrição, conteúdo e tags usando fuzzy search."""
    if not query.strip():
        raise ValueError("query não pode ser vazia")
    limit = max(1, min(limit, 50))
    wanted_tags = {_normalize(tag) for tag in (tags or [])}
    results = []
    for note in _index():
        note_tags = {_normalize(tag) for tag in note.get("tags", [])}
        if wanted_tags and not wanted_tags.issubset(note_tags):
            continue
        content = ""
        if include_content:
            content = _get(f"{RAW_ROOT}/{_validate_path(note['path'])}")
        score = _score(query, note, content)
        if score >= 0.18:
            item = {**note, "score": score}
            if include_content:
                item["content"] = content
            results.append(item)
    results.sort(key=lambda item: (-item["score"], item.get("date", "")), reverse=False)
    return {"query": query, "count": len(results[:limit]), "results": results[:limit]}


@mcp.tool()
def get_note(slug: str | None = None, path: str | None = None) -> dict[str, Any]:
    """Retorna o conteúdo completo de uma nota por slug ou caminho relativo."""
    if not slug and not path:
        raise ValueError("informe slug ou path")
    note = next((item for item in _index() if (slug and item.get("slug") == slug) or (path and item.get("path") == path)), None)
    if not note:
        raise ValueError("nota não encontrada")
    return {**note, "content": _get(f"{RAW_ROOT}/{_validate_path(note['path'])}")}


@mcp.tool()
def list_tags(query: str | None = None, limit: int = 100) -> dict[str, Any]:
    """Lista tags únicas; opcionalmente filtra tags com fuzzy search."""
    tags = sorted({tag for note in _index() for tag in note.get("tags", [])})
    if query:
        normalized = _normalize(query)
        tags = sorted(tags, key=lambda tag: SequenceMatcher(None, normalized, _normalize(tag)).ratio(), reverse=True)
        tags = [tag for tag in tags if SequenceMatcher(None, normalized, _normalize(tag)).ratio() >= 0.35]
    return {"count": min(len(tags), limit), "tags": tags[: max(1, min(limit, 500))]}


@mcp.tool()
def list_notes(tag: str | None = None, limit: int = 50) -> dict[str, Any]:
    """Lista notas, opcionalmente filtradas por uma tag exata."""
    notes = _index()
    if tag:
        normalized = _normalize(tag)
        notes = [note for note in notes if normalized in {_normalize(item) for item in note.get("tags", [])}]
    return {"count": min(len(notes), limit), "notes": notes[: max(1, min(limit, 100))]}


@mcp.prompt()
def build_project_context(project: str, query: str, limit: int = 8) -> str:
    """Monta instruções para usar notas recuperadas como contexto de um projeto."""
    result = search_notes(query, limit=limit, include_content=True)
    sources = "\n\n".join(
        f"## {item['slug']}\nFonte: {item['path']}\nTags: {', '.join(item.get('tags', []))}\n\n{item.get('content', '')}"
        for item in result["results"]
    )
    return (
        f"Você está construindo o projeto: {project}.\n"
        "Use as notas abaixo como contexto e referências, não como fatos atuais garantidos. "
        "Preserve a atribuição das fontes e sinalize lacunas ou informações que precisam ser verificadas.\n\n"
        f"Consulta: {query}\n\n{sources}"
    )


if __name__ == "__main__":
    mcp.run()
