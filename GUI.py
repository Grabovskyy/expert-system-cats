# app.py
import streamlit as st
import subprocess
from KOTY_razem import wybierz_kota, rozmiar_kota_wedlug_wagi, Cena_kota, utrzymanie

st.set_page_config(page_title="🐱 Dobór kota", layout="centered")
st.title("🐱 Wybierz idealnego kota!")

st.markdown("""
To jest interaktywne narzędzie do wyboru kota.  
Możesz wprowadzić cechy kota i własne preferencje, a silnik zwróci **Top 3 koty** najlepiej dopasowane.
""")

# =========================
# 1️⃣ Dane fizyczne kota
# =========================
st.subheader("1️⃣ Dane kota (dla obliczeń rozmiaru i ceny)")

waga = st.number_input("Waga kota (kg)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
wiek = st.number_input("Wiek kota (lata)", min_value=0.1, max_value=20.0, value=2.0, step=0.1)
plec = st.selectbox("Płeć kota", ["samiec", "samica"])

# =========================
# 2️⃣ Preferencje użytkownika
# =========================
st.subheader("2️⃣ Preferencje dla systemu ekspertowego")

dlugosc_siersci = st.selectbox("Długość sierści", ["Krótka", "Średnia", "Długa"])
charakter = st.selectbox("Charakter", ["Spokojny", "Zabawowy", "Niezależny"])
hipoalergiczny = st.selectbox("Hipoalergiczny?", ["Tak", "Nie"])
towarzyskosc_slider = st.slider("Poziom towarzyskości (1-10)", 1, 10, 5)
towarzyskosc = ("Niska" if towarzyskosc_slider <= 3 else "Umiarkowana" if towarzyskosc_slider <= 7 else "Wysoka")
aktywnosc_slider = st.slider("Poziom aktywności (1-10)", 1, 10, 5)
aktywnosc = "Niska" if aktywnosc_slider <= 3 else "Umiarkowana" if aktywnosc_slider <= 7 else "Wysoka"

# =========================
# 3️⃣ Wywołanie silnika
# =========================
if st.button("Oblicz Top 3 koty"):

    # Obliczenie rozmiaru i ceny przez funkcje customowe
    rozmiar = rozmiar_kota_wedlug_wagi(waga)
    cena = Cena_kota(waga, wiek, plec)
    koszt = utrzymanie(rozmiar, dlugosc_siersci, aktywnosc)

    # Przygotowanie profilu dla wybierz_kota
    profil = {
        "rozmiar": rozmiar,
        "dlugosc_siersci": dlugosc_siersci,
        "aktywnosc": aktywnosc,
        "towarzyskosc": towarzyskosc,
        "hipoalergiczny": hipoalergiczny,
        "charakter": charakter,
        "Cena": cena
    }

    # Wywołanie systemu ekspertowego
    wynik = wybierz_kota(profil)

    # Wyświetlenie wyników Top 3
    st.subheader("🏆 Top 3 koty")
    for i, kot in enumerate(wynik["top3"], start=1):
        st.markdown(f"**{i}. {kot['name']}** – punkty: {kot['score']}")
        for r in kot["reasons"]:
            st.markdown(f"   - {r}")

    st.subheader("💰 Szacunkowa cena i koszty utrzymania")
    st.write(f"Rozmiar kota wg wagi: **{rozmiar}**")
    st.write(f"Szacowana cena: **{cena} zł**")
    st.write(f"Szacowany koszt utrzymania: **{koszt}**")


# =========================
# 4️⃣ Uruchamianie testów Pytest
# =========================
st.sidebar.header("🧪 Testy")
if st.sidebar.button("Uruchom wszystkie testy"):
    st.sidebar.info("Uruchamianie testów, proszę czekać…")
    try:
        # uruchomienie pytest dla wszystkich plików testowych w katalogu
        result = subprocess.run(
            ["pytest", "-q", "--tb=short"],  # usuń nazwę pliku, jeśli chcesz wszystkie testy w katalogu
            capture_output=True, text=True
        )

        # wyświetlenie wyjścia w Streamlit
        st.text(result.stdout)

        st.text(result.stderr)

        if result.returncode == 0:
            st.success("Wszystkie testy przeszły pomyślnie! ✅")
        else:
            st.error(f"Niektóre testy nie przeszły! Kod wyjścia: {result.returncode}")
    
    except Exception as e:
        st.error(f"Wystąpił błąd podczas uruchamiania testów: {e}")