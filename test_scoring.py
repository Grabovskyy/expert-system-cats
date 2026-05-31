from KOTY_razem import wybierz_kota

def test_top3_length():
    """Sprawdza, czy silnik zawsze zwraca dokładnie 3 propozycje kotów."""
    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Krótka",
        "aktywnosc": "Wysoka",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Tak",
        "charakter": "Zabawowy"
    }
    wynik = wybierz_kota(profil)
    assert len(wynik["top3"]) == 3

def test_scores_sorted_desc():
    """Sprawdza, czy ranking kotów jest poprawnie posortowany (od najwyższego wyniku)."""
    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Długa",
        "aktywnosc": "Niska",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Nie",
        "charakter": "Spokojny"
    }
    scores = [c["score"] for c in wybierz_kota(profil)["top3"]]
    # Sprawdzamy, czy lista punktów jest identyczna z jej posortowaną malejąco wersją
    assert scores == sorted(scores, reverse=True)

def test_scores_non_negative():
    """Sprawdza, czy żaden kot nie dostał ujemnych punktów."""
    profil = {
        "rozmiar": "Duży",
        "dlugosc_siersci": "Długa",
        "aktywnosc": "Wysoka",
        "towarzyskosc": "Umiarkowana",
        "hipoalergiczny": "Nie",
        "charakter": "Niezależny"
    }
    for c in wybierz_kota(profil)["top3"]:
        assert c["score"] >= 0
