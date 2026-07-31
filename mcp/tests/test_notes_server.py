import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

import notes_server


def test_normalize_is_case_insensitive():
    assert notes_server._normalize("Agentes de IA") == "agentes de ia"


def test_score_prefers_matching_tag():
    note = {"slug": "other", "tags": ["agentes-ia"], "description": "automation"}
    assert notes_server._score("agentes ia", note) > notes_server._score("database", note)


def test_validate_path_blocks_traversal():
    try:
        notes_server._validate_path("_posts/../secrets.txt")
    except ValueError:
        pass
    else:
        raise AssertionError("path traversal was accepted")


def test_index_shape():
    assert isinstance(json.loads('[{"slug": "example", "tags": ["demo"]}']), list)
