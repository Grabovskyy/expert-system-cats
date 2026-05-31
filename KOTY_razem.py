import json
import rule_engine
import datetime

# ==================================================
# CUSTOMOWE FUNKCJE SYSTEMU EKSPERTOWEGO
# ==================================================

def waliduj_profil(profil):

    DOZWOLONE_ROZMIARY = ["Mały", "Średni", "Duży"]
    DOZWOLNE_DLUGOSCI_SIERSCI = ["Krótka", "Średnia", "Długa"]
    DOZWOLNE_AKTYWNOSCI = ["Niska", "Umiarkowana", "Średnia", "Wysoka"]
    DOZWOLNE_TOWARZYSKOSCI = ["Niska", "Umiarkowana", "Średnia", "Wysoka"]
    DOZWOLNE_HIPOALERGICZNE = ["Tak", "Nie"]
    DOZWOLNE_CHARAKTERY = ["Zabawowy", "Spokojny", "Niezależny"]


    wymagane_klucze = ["rozmiar", "dlugosc_siersci", "aktywnosc", "towarzyskosc", "hipoalergiczny", "charakter"]
    if not isinstance(profil, dict):
        raise TypeError("Profil musi być słownikiem!")

    for k in wymagane_klucze:
        if k not in profil:
            raise KeyError(f"Brak wymaganego klucza: {k}")
        if profil[k] is None:
            raise ValueError(f"Atrybut '{k}' nie może być None")
        if not isinstance(profil[k], str):
            raise TypeError(f"Atrybut '{k}' musi być tekstem, otrzymano {type(profil[k]).__name__}")

    # Sprawdzenie dopuszczalnych wartości
    if profil["rozmiar"] not in DOZWOLONE_ROZMIARY:
        raise ValueError(f"Nieznana wartość rozmiaru: {profil['rozmiar']}")
    if profil["dlugosc_siersci"] not in DOZWOLNE_DLUGOSCI_SIERSCI:
        raise ValueError(f"Nieznana wartość długości sierści: {profil['dlugosc_siersci']}")
    if profil["aktywnosc"] not in DOZWOLNE_AKTYWNOSCI:
        raise ValueError(f"Nieznana wartość aktywności: {profil['aktywnosc']}")
    if profil["towarzyskosc"] not in DOZWOLNE_TOWARZYSKOSCI:
        raise ValueError(f"Nieznana wartość towarzyskosci: {profil['towarzyskosc']}")
    if profil["hipoalergiczny"] not in DOZWOLNE_HIPOALERGICZNE:
        raise ValueError(f"Nieznana wartość hipoalergiczny: {profil['hipoalergiczny']}")
    if profil["charakter"] not in DOZWOLNE_CHARAKTERY:
        raise ValueError(f"Nieznana wartość charakteru: {profil['charakter']}")

def rozmiar_kota_wedlug_wagi(waga):
    """
    Określa rozmiar kota na podstawie wagi (kg)
    """
    if waga <= 3:
        return "Mały"
    elif waga <= 6:
        return "Średni"
    else:
        return "Duży"


def Cena_kota(waga, wiek, plec):
    """
    Szacunkowa cena kota na podstawie cech fizycznych
    """
    if plec == "samiec":
        baza = 500
    elif plec == "samica":
        baza = 1000

    if wiek <= 0:
        wiek = 1  # zabezpieczenie

    cena = (waga * 20) / wiek + baza
    return round(cena, 2)


def utrzymanie(rozmiar, dlugosc_siersci, aktywnosc):
    """
    Określa koszt utrzymania kota na podstawie cech
    """
    if rozmiar == "Duży":
        if dlugosc_siersci == "Długa" or aktywnosc == "Wysoka":
            return "Wysoki"
        return "Średni"

    if rozmiar == "Mały":
        if aktywnosc == "Niska" and dlugosc_siersci == "Krótka":
            return "Niski"
        return "Średni"

    return "Średni"


# ==================================================
# WCZYTANIE BAZY WIEDZY (JSON)
# ==================================================

with open("cats.json", "r", encoding="utf-8") as f:
    cats = json.load(f)


# ==================================================
# REJESTR FUNKCJI DLA rule_engine
# ==================================================

CUSTOM_FUNCTIONS = {
    "rozmiar_kota_wedlug_wagi": rozmiar_kota_wedlug_wagi,
    "Cena_kota": Cena_kota,
    "utrzymanie": utrzymanie
}


def resolver(thing, name):
    # zmienne wejściowe (fakty)
    if name in thing:
        return thing[name]

    # funkcje własne
    if name in CUSTOM_FUNCTIONS:
        return CUSTOM_FUNCTIONS[name]

    raise KeyError(name)


context = rule_engine.Context(resolver=resolver)


# ==================================================
# SILNIK WNIOSKOWANIA
# ==================================================

def wybierz_kota(preferencje):
    waliduj_profil(preferencje)
    ranking = []

    for cat in cats:
        score = 0
        reasons = []

        for rule_data in cat["rules"]:
            expr = rule_data["expr"]
            pts = rule_data["pts"]
            explanation = rule_data["explanation"]

            rule = rule_engine.Rule(expr)
            if rule.matches(preferencje):
                score += pts
                reasons.append(f"+{pts} pkt: {explanation}")

        ranking.append({
            "name": cat["name"],
            "score": score,
            "reasons": reasons
        })

    ranking.sort(key=lambda x: x["score"], reverse=True)

    top3 = ranking[:3]
    max_score = top3[0]["score"]

    wyjasnienia = ""
    for cat in top3:
        if cat["score"] == max_score:
            wyjasnienia += f"\nWyjaśnienie dla {cat['name']}:\n"
            for r in cat["reasons"]:
                wyjasnienia += f"  • {r}\n"

    return {
        "top3": top3,
        "wyjasnienia": wyjasnienia
    }


# ==================================================
# PRZYKŁADOWE DANE UŻYTKOWNIKA
# ==================================================

cena = Cena_kota(
    waga=10,
    wiek=4,
    plec="samiec"
)

koszt = utrzymanie(
    rozmiar="Mały",
    dlugosc_siersci="Długa",
    aktywnosc="Wysoka"
)

profil = {
    "rozmiar": rozmiar_kota_wedlug_wagi(5),
    "dlugosc_siersci": "Krótka",
    "aktywnosc": "Wysoka",
    "towarzyskosc": "Wysoka",
    "hipoalergiczny": "Tak",
    "charakter": "Zabawowy",
    "Cena": cena
}


# ==================================================
# URUCHOMIENIE SYSTEMU
# ==================================================

print(f"Szacowana cena kota: {cena} zł\n")
print(f"Szacowany koszt utrzymania: {koszt}\n")

wynik = wybierz_kota(profil)

print("TOP 3 KOTÓW:\n")
for i, kot in enumerate(wynik["top3"], 1):
    print(f"{i}. {kot['name']} — {kot['score']} pkt")
    for r in kot["reasons"]:
        print("   ", r)
    print()

print("\n=== WYJAŚNIENIA ===")
print(wynik["wyjasnienia"])
