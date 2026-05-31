import rule_engine

rules = [
    ("Maine Coon", rule_engine.Rule('rozmiar == "Duży" and długość_siersci == "Długa" and aktywność == "Umiarkowana" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Syjamski", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Wysoka" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Zabawowy"')),
    ("Bengalski", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Wysoka" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Niezależny"')),
    ("Sfinks", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Umiarkowana" and towarzyskość == "Wysoka" and hipoalergiczny == "Tak" and charakter == "Zabawowy"')),
    ("Ragdoll", rule_engine.Rule('rozmiar == "Duży" and długość_siersci == "Długa" and aktywność == "Niska" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Brytyjski Krótkowłosy", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Niska" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Norweski Leśny", rule_engine.Rule('rozmiar == "Duży" and długość_siersci == "Długa" and aktywność == "Wysoka" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Niezależny"')),
    ("Rosyjski Niebieski", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Umiarkowana" and towarzyskość == "Niska" and hipoalergiczny == "Tak" and charakter == "Spokojny"')),
    ("Pers", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Długa" and aktywność == "Niska" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Devon Rex", rule_engine.Rule('rozmiar == "Mały" and długość_siersci == "Krótka" and aktywność == "Wysoka" and towarzyskość == "Wysoka" and hipoalergiczny == "Tak" and charakter == "Zabawowy"')),
    ("Cornish Rex", rule_engine.Rule('rozmiar == "Mały" and długość_siersci == "Krótka" and aktywność == "Wysoka" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Tak" and charakter == "Zabawowy"')),
    ("Scottish Fold", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Średnia" and aktywność == "Niska" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Abisyński", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Wysoka" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Niezależny"')),
    ("Somalijski", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Długa" and aktywność == "Wysoka" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Zabawowy"')),
    ("Orientalny Krótkowłosy", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Umiarkowana" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Zabawowy"')),
    ("Birman", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Długa" and aktywność == "Niska" and towarzyskość == "Wysoka" and hipoalergiczny == "Nie" and charakter == "Spokojny"')),
    ("Balinese", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Średnia" and aktywność == "Umiarkowana" and towarzyskość == "Wysoka" and hipoalergiczny == "Tak" and charakter == "Zabawowy"')),
    ("LaPerm", rule_engine.Rule('rozmiar == "Mały" and długość_siersci == "Średnia" and aktywność == "Umiarkowana" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Tak" and charakter == "Spokojny"')),
    ("Chartreux", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Krótka" and aktywność == "Niska" and towarzyskość == "Niska" and hipoalergiczny == "Nie" and charakter == "Niezależny"')),
    ("Manx", rule_engine.Rule('rozmiar == "Średni" and długość_siersci == "Średnia" and aktywność == "Umiarkowana" and towarzyskość == "Umiarkowana" and hipoalergiczny == "Nie" and charakter == "Niezależny"'))
]


def wybierz_gatunek_ksiazki(preferencje):
    for nazwa, reg in rules:
        if reg.matches(preferencje):
            return nazwa
    return "Brak dopasowania"

#Gatunek High Fantsy
preferencje_czytelnika = {
    "cel_czytania": "Relaks i ucieczka",
    "szukasz_wrazen": "Nie",
    "lekkosc_i_humor": "Nie",
    "realny_czy_fantastyczny": "Świat fantastyczny" 
}

print(wybierz_gatunek_ksiazki(preferencje_czytelnika))  # → High Fantasy

print(rule_engine.__version__)
