from KOTY_razem import wybierz_kota

def test_full_flow():
    """
    Testuje pełny przepływ działania systemu eksperckiego:
    od profilu użytkownika do top3 kotów i wyjaśnień.
    """

    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Krótka",
        "aktywnosc": "Wysoka",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Tak",
        "charakter": "Zabawowy"
    }

    wynik = wybierz_kota(profil)

    # Sprawdzenie, czy wynik ma poprawną strukturę
    assert "top3" in wynik
    assert "wyjasnienia" in wynik
    assert len(wynik["top3"]) == 3
    assert wynik["top3"][0]["score"] > 0
