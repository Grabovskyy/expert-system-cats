import pytest
import json
from pathlib import Path

def test_missing_json_file():
    """
    Testuje sytuację, gdy plik JSON nie istnieje
    """
    non_existent_path = Path("/nonexistent/path/cats.json")
    with pytest.raises(FileNotFoundError):
        with open(non_existent_path, "r", encoding="utf-8") as f:
            json.load(f)

def test_invalid_json_syntax(tmp_path):
    """
    Testuje sytuację, gdy plik JSON jest uszkodzony
    """
    json_file = tmp_path / "invalid.json"
    # zapisujemy uszkodzony JSON
    json_file.write_text("{uszkodzony json,,,}")
    with pytest.raises(json.JSONDecodeError):
        with open(json_file, "r", encoding="utf-8") as f:
            json.load(f)
