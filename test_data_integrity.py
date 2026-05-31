import json
import pytest
from KOTY_razem import cats

class TestDataIntegrity:
    """Testy spójności i integralności bazy danych kotów"""

    def test_json_structure_valid(self):
        # Sprawdzenie, czy dane wczytane są jako lista i nie są puste
        assert isinstance(cats, list)
        assert len(cats) > 0

    def test_each_cat_has_required_fields(self):
        # Każdy kot powinien mieć 'name' i 'rules', a rules musi być listą
        for cat in cats:
            assert "name" in cat, f"Kot {cat} missing 'name'"
            assert "rules" in cat, f"Kot {cat} missing 'rules'"
            assert isinstance(cat["rules"], list), f"Kot {cat} -> 'rules' musi być listą"

    def test_no_duplicate_cat_names(self):
        # Żadna rasa kota nie może się powtarzać
        names = [c["name"] for c in cats]
        assert len(names) == len(set(names)), "Znaleziono duplikaty nazw kotów!"
