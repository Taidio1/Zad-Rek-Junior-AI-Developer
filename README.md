# Generator HTML na podstawie artykułu tekstowego

## Opis

Ten projekt to aplikacja w języku Python, która wykorzystuje API OpenAI do generowania kodu HTML na podstawie treści artykułu zawartego w pliku tekstowym.
Aplikacja odczytuje artykuł, przetwarza go zgodnie z określonymi wytycznymi i zapisuje wygenerowany kod HTML do nowego pliku.

### Funkcjonalności

- Odczyt artykułu z pliku tekstowego.
- Generowanie kodu HTML zgodnie z wytycznymi.
- Zapis wygenerowanego kodu HTML do pliku.

## Wymagania

- Python 3.x.
- Zainstalowana biblioteka `openai`.
- Klucz API OpenAI.

## Instalacja

1. **Zainstaluj Python**: Upewnij się, że masz zainstalowany Python w wersji 3.x.

2. **Zainstaluj bibliotekę OpenAI**: Użyj poniższego polecenia w termialu, aby zainstalować bibliotekę OpenAI:<br>
   pip install openai

## Uruchomienie
1. **Ustaw klucz API OpenAI**: Zastąp `YOUR_API_KEY`
2. **Wygeneruj artykuł z pliku txt**: w terminalu wpisz ```python app.py ``` (artykul.html został już wcześniej wygenerowany)

### Dodatkowe Funckje (+Branch: Playground)
Branch: Main
- Wygenerowanie szablonu HTML do podglądu artykułu

Branch: Playground
- Mierzenie czasu i liczenie tokenów (zapisywane w osobnym pliku .txt).
- Walidacja wygenerowanej strony – zaimplementowałem funkcję, która sprawdza wygenerowaną stronę pod kątem obecności niepotrzebnych tagów, aby zapewnić jej czystość i zgodność z wymaganiami.
   - Mimo początkowych instrukcji w promptach, aby AI nie dodawało kodu ,,```html ,, oraz ,, ``,, na początku i końcu strony, zauważyłem, że 1/4 prób zawierały błędne dane. Przeprowadziłem poprawki w algorytmie, eliminując ten problem.
