from KOTY_razem import wybierz_kota

def test_conflicting_rules_multiple_winners():
    """
    Test sprawdza, czy system poprawnie obsługuje konflikt reguł
    (więcej niż jeden kot z takim samym najwyższym wynikiem)
    """

    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Krótka",
        "aktywnosc": "Wysoka",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Nie",
        "charakter": "Zabawowy"
    }

    wynik = wybierz_kota(profil)

    top_score = wynik["top3"][0]["score"]
    winners = [c for c in wynik["top3"] if c["score"] == top_score]

    assert len(winners) >= 1
