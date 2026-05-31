# expert-system-cats
application for a pass in expert systems at university
<img width="1909" height="910" alt="image" src="https://github.com/user-attachments/assets/a1fe263f-6d0f-47ba-b4f5-ba27049d2485" />
# 🐱 System Ekspertowy: Dobór Idealnego Kota

Interaktywna aplikacja webowa napisana w języku Python, wykorzystująca framework **Streamlit** oraz bibliotekę **rule-engine** do stworzenia systemu ekspertowego. Program pomaga przyszłym właścicielom w wyborze idealnej rasy kota na podstawie wprowadzonych danych fizycznych oraz osobistych preferencji.

## ✨ Funkcje projektu

* **Interaktywny interfejs (GUI):** Zbudowany w oparciu o Streamlit, pozwalający na łatwe i intuicyjne wprowadzanie danych za pomocą suwaków i list rozwijanych.
* **Silnik wnioskowania:** Oblicza dopasowanie ras kotów z bazy wiedzy (plik JSON) na podstawie zaawansowanych reguł (`rule-engine`).
* **Kalkulacje kosztów i rozmiaru:** Program automatycznie szacuje wielkość kota, jego rynkową cenę oraz koszty utrzymania na podstawie wagi, wieku i innych cech.
* **Rekomendacja Top 3:** Zwraca 3 najlepiej dopasowane rasy wraz ze szczegółowym wyjaśnieniem przyznanej punktacji.
* **Wbudowane testy:** Możliwość uruchomienia testów jednostkowych (Pytest) bezpośrednio z paska bocznego aplikacji.

## 📂 Struktura plików

* `GUI.py` — Główny plik aplikacji Streamlit obsługujący interfejs użytkownika.
* `KOTY_razem.py` — Logika systemu ekspertowego, funkcje walidacyjne, szacujące (cena, koszt utrzymania) oraz konfiguracja silnika reguł.
* `cats.json` — Baza wiedzy (Knowledge Base) w formacie JSON, zawierająca rasy kotów, przypisane im reguły i punktację.
* `program.py` — Przykładowy skrypt testowy pokazujący działanie biblioteki `rule-engine`.
* `AST.py` — Skrypt narzędziowy do podglądu Drzewa Składniowego (Abstract Syntax Tree) reguł silnika.
* `requirements.txt` — Lista wymaganych bibliotek Pythona do uruchomienia projektu.
* reszta to testy~~

## 🛠️ Wymagania i instalacja

Aby uruchomić aplikację lokalnie, musisz mieć zainstalowanego Pythona (zalecana wersja 3.8+).

**pip install -r requirements.txt**

🚀 Uruchomienie aplikacji
Aby włączyć interfejs graficzny, upewnij się, że znajdujesz się w katalogu z plikami projektu i wpisz w terminalu następującą komendę:

streamlit run GUI.py
