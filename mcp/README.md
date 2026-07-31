# Notes MCP

Servidor MCP para pesquisar e reutilizar os conteúdos de [`ronanrodrigo/notes`](https://github.com/ronanrodrigo/notes).

## Recursos

* `search_notes`: fuzzy search em slug, tags, descrição e, opcionalmente, conteúdo completo.
* `get_note`: recupera uma nota completa por `slug` ou `path`.
* `list_tags`: lista tags e permite fuzzy filtering.
* `list_notes`: lista notas, com filtro opcional por tag.
* `build_project_context`: prompt que monta contexto rastreável para iniciar um projeto.

O índice é lido de `index.json`, enquanto o conteúdo é baixado sob demanda dos posts em `_posts/`. Assim, novas notas ficam disponíveis sem manter um índice duplicado no MCP.

## Instalação local

```bash
cd mcp
python -m venv .venv
source .venv/bin/activate
pip install -e .
python notes_server.py
```

Para repositório privado ou para reduzir limites da API, defina `GITHUB_TOKEN`. Também é possível configurar `NOTES_GITHUB_OWNER`, `NOTES_GITHUB_REPO` e `NOTES_GITHUB_REF`.

## Configuração em clientes MCP

Exemplo para clientes que aceitam servidores via stdio:

```json
{
  "mcpServers": {
    "ronanrodrigo-notes": {
      "command": "python",
      "args": ["/caminho/absoluto/notes/mcp/notes_server.py"]
    }
  }
}
```

## Fluxo recomendado para construir projetos

1. Use `search_notes` com uma consulta ampla e tags relevantes.
2. Use `get_note` para aprofundar as fontes selecionadas.
3. Use `build_project_context` para obter um contexto inicial com caminhos de origem.
4. Valide links, versões, custos e afirmações atuais antes de implementar.
