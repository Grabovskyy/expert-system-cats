import rule_engine

def test_rule_positive_match():
    rule = rule_engine.Rule("rozmiar == 'Średni' and aktywnosc == 'Wysoka'")
    data = {"rozmiar": "Średni", "aktywnosc": "Wysoka"}
    assert rule.matches(data)

def test_rule_negative_match():
    rule = rule_engine.Rule("rozmiar == 'Średni' and aktywnosc == 'Wysoka'")
    data = {"rozmiar": "Duży", "aktywnosc": "Wysoka"}
    assert not rule.matches(data)

def test_rule_in_operator():
    rule = rule_engine.Rule("charakter in ['Zabawowy', 'Niezależny']")
    assert rule.matches({"charakter": "Zabawowy"})
    assert rule.matches({"charakter": "Niezależny"})
    assert not rule.matches({"charakter": "Spokojny"})

def test_rule_not_equal():
    rule = rule_engine.Rule("hipoalergiczny != 'Tak'")
    assert rule.matches({"hipoalergiczny": "Nie"})
    assert not rule.matches({"hipoalergiczny": "Tak"})
