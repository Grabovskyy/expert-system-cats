from KOTY_razem import wybierz_kota

def test_syjamski_still_top_for_active_high_friendliness():
    """
    Sprawdza, czy Syjamski pozostaje w top3 dla profilu bardzo aktywnego i towarzyskiego.
    """

    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Krótka",
        "aktywnosc": "Wysoka",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Nie",
        "charakter": "Zabawowy"
    }

    names = [c["name"] for c in wybierz_kota(profil)["top3"]]
    assert "Syjamski" in names

def test_sfinks_top_for_hypoallergenic_profile():
    """
    Sprawdza, czy Sfinks pozostaje w top3 dla profilu hipoalergicznego i kontaktowego.
    """

    profil = {
        "rozmiar": "Średni",
        "dlugosc_siersci": "Krótka",
        "aktywnosc": "Umiarkowana",
        "towarzyskosc": "Wysoka",
        "hipoalergiczny": "Tak",
        "charakter": "Zabawowy"
    }

    names = [c["name"] for c in wybierz_kota(profil)["top3"]]
    assert "Sfinks" in names
