import itertools
from KOTY_razem import wybierz_kota

def test_all_possible_combinations_do_not_crash():
    """
    Sprawdza, czy silnik działa dla KAŻDEJ kombinacji parametrów kota.
    """

    rozmiar = ["Mały", "Średni", "Duży"]
    dlugosc_siersci = ["Krótka", "Średnia", "Długa"]
    aktywnosc = ["Niska", "Umiarkowana", "Wysoka"]
    towarzyskosc = ["Niska", "Umiarkowana", "Wysoka"]
    hipoalergiczny = ["Tak", "Nie"]
    charakter = ["Spokojny", "Zabawowy", "Niezależny"]

    combinations = list(itertools.product(
        rozmiar, dlugosc_siersci, aktywnosc, towarzyskosc, hipoalergiczny, charakter
    ))

    for combo in combinations:
        profil = {
            "rozmiar": combo[0],
            "dlugosc_siersci": combo[1],
            "aktywnosc": combo[2],
            "towarzyskosc": combo[3],
            "hipoalergiczny": combo[4],
            "charakter": combo[5]
        }

        wynik = wybierz_kota(profil)

        # Sprawdzenie, czy wynik istnieje i top3 jest poprawny
        assert "top3" in wynik
        assert len(wynik["top3"]) == 3
        assert all(c["score"] >= 0 for c in wynik["top3"])

if __name__ == "__main__":
    test_all_possible_combinations_do_not_crash()
    print("Przetestowano wszystkie kombinacje parametrów kota - brak crashy!")
