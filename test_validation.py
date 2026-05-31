import pytest
from KOTY_razem import wybierz_kota

class TestValidation:
    """Testy walidacji danych wejściowych dla silnika kotów"""

    def test_empty_profile(self):
        """Pusty profil powinien rzucić błąd, bo brakuje kluczy do reguł"""
        with pytest.raises((ValueError, KeyError, TypeError)):
            wybierz_kota({})

    def test_none_profile(self):
        """Sprawdza, czy silnik padnie przy podaniu None"""
        with pytest.raises((ValueError, TypeError, AttributeError)):
            wybierz_kota(None)

    def test_invalid_attribute_value(self):
        """Nieznana wartość (np. rozmiar, którego nie ma w JSON)"""
        profile = {
            "rozmiar": "gigantyczny", # Nieznana wartość
            "dlugosc_siersci": "MegaDługa", # Nieistniejąca
            "aktywnosc": "Kosmiczna",
            "towarzyskosc": "Wysoka",
            "hipoalergiczny": "Tak",
            "charakter": "Zabawowy"
        }
        # Ten test przejdzie (wynik 0 pkt), chyba że wymusisz błąd w kodzie
        with pytest.raises((ValueError, KeyError)):
            wybierz_kota(profile)

    def test_missing_required_attributes(self):
        """Brak wymaganych kluczy w słowniku"""
        profile = {
            "rozmiar": "Średni",
            "aktywnosc": "Wysoka"
        }
        with pytest.raises((ValueError, KeyError)):
            wybierz_kota(profile)

    def test_type_mismatch_number_instead_of_string(self):
        """Liczba tam, gdzie powinien być tekst"""
        profile = {
            "rozmiar": 123,
            "dlugosc_siersci": "Krótka",
            "aktywnosc": "Wysoka",
            "towarzyskosc": "Wysoka",
            "hipoalergiczny": "Tak",
            "charakter": "Zabawowy"
        }
        with pytest.raises((TypeError, ValueError)):
            wybierz_kota(profile)

    def test_extra_unknown_attributes_should_be_ignored(self):
        """Dodatkowe śmieciowe dane nie powinny psuć wyniku"""
        profile = {
            "rozmiar": "Mały",
            "dlugosc_siersci": "Krótka",
            "aktywnosc": "Wysoka",
            "towarzyskosc": "Wysoka",
            "hipoalergiczny": "Tak",
            "charakter": "Zabawowy",
            "dodatkowy_info": "jestem fanem",
            "wiek": 21
        }
        result = wybierz_kota(profile)
        assert "top3" in result

    def test_null_values_in_attributes(self):
        """None/null zamiast konkretnej wartości atrybutu"""
        profile = {
            "rozmiar": None,
            "dlugosc_siersci": "Krótka",
            "aktywnosc": "Wysoka",
            "towarzyskosc": "Wysoka",
            "hipoalergiczny": "Tak",
            "charakter": "Zabawowy"
        }
        with pytest.raises((TypeError, ValueError)):
            wybierz_kota(profile)
