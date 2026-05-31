import pytest
from KOTY_razem import (
    rozmiar_kota_wedlug_wagi,
    Cena_kota,
    utrzymanie
)

class TestBusinessLogicAccuracy:
    """Testy dokładności logiki systemu ekspertowego (koty)"""

    def test_cena_kota_dokladna(self):
        """
        Test dokładności obliczania ceny kota
        """
        cena = Cena_kota(
            waga=10,
            wiek=4,
            plec="samiec"
        )

        # (10 * 20) / 4 + 500 = 550
        assert cena == pytest.approx(550.0, rel=0.01)

    def test_rozmiar_kota_duzy(self):
        """
        Test poprawnej klasyfikacji rozmiaru kota
        """
        rozmiar = rozmiar_kota_wedlug_wagi(8)
        assert rozmiar == "Duży"

    def test_koszt_utrzymania_wysoki(self):
        """
        Test kosztu utrzymania dla dużego, aktywnego kota z długą sierścią
        """
        koszt = utrzymanie(
            rozmiar="Duży",
            dlugosc_siersci="Długa",
            aktywnosc="Wysoka"
        )
        assert koszt == "Wysoki"
