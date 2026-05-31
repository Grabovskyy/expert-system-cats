import pytest
from KOTY_razem import Cena_kota, utrzymanie, rozmiar_kota_wedlug_wagi

def test_cena_kota_dla_roznych_parametrow():
    # samiec, waga=10, wiek=4
    assert Cena_kota(10, 4, "samiec") == pytest.approx(550.0, rel=0.01)
    # samica, waga=5, wiek=2
    assert Cena_kota(5, 2, "samica") == pytest.approx(1050.0, rel=0.01)

def test_utrzymanie_dla_roznych_parametrow():
    # duży, długa sierść, wysoka aktywność
    assert utrzymanie("Duży", "Długa", "Wysoka") == "Wysoki"
    # mały, krótka sierść, niska aktywność
    assert utrzymanie("Mały", "Krótka", "Niska") == "Niski"
    # średni, średnia sierść, umiarkowana aktywność
    assert utrzymanie("Średni", "Średnia", "Umiarkowana") == "Średni"

def test_rozmiar_kota_wedlug_wagi():
    assert rozmiar_kota_wedlug_wagi(2) == "Mały"
    assert rozmiar_kota_wedlug_wagi(4) == "Średni"
    assert rozmiar_kota_wedlug_wagi(8) == "Duży"
