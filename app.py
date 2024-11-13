"""
Program do generowania kodu HTML na podstawie artykułu tekstowego.

Ten skrypt wykorzystuje API OpenAI do przetwarzania treści artykułu zawartego w pliku tekstowym 
i generowania odpowiedniego kodu HTML zgodnie z określonymi wytycznymi. 

Uwaga: Klucz API OpenAI nie wpisany z wracji bezpieczeństwa.
"""

import openai

# Funkcja do odczytu pliku tekstowego
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Funkcja do komunikacji z API OpenAI
def generate_html(article_content, prompt):
    api_key = 'OPENAI_API_KEY'
    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "Jesteś pomocnym asystentem i świetnym programistą, który generuje kod HTML na podstawie przesłanych artykułów txt."},
        {"role": "user", "content": f"{prompt}\n\n{article_content}"}
    ]

    response = openai.ChatCompletion.create(
        model='gpt-4o', 
        messages=messages,
        max_tokens=1500
    )
    
    return response.choices[0].message['content']

# Funkcja do zapisania wygenerowanego HTML do pliku
def save_html_to_file(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Główna funkcja
def main():
    article_path = 'article.txt' 
    html_output_path = 'artykul.html'
    prompt = """Proszę wygenerować kod HTML dla poniższego artykułu w języku polskim, przestrzegając następujących wytycznych:
    1. **Struktura treści**: Wykorzystaj odpowiednie tagi HTML do strukturyzacji artykułu, takie jak <h1>, <h2>, <p>, <ul>, <li> i inne, aby odzwierciedlić logiczny podział i hierarchię treści artykułu.
    2. **Obrazki**: Wskaż miejsca, w których warto umieścić grafikę, dodając:
   - Tag <img> z atrybutem src="image_placeholder.jpg" w miejscach, gdzie obrazki będą wizualnie wzbogacać treść.
   - Dodaj atrybut alt do każdego obrazka jako prompt, który będzie dokładnie opisywać treść obrazka w języku polskim. 
   - Umieść podpis pod każdym obrazkiem, korzystając z odpowiedniego tagu HTML, np. <figcaption>.
    3. **Bez dodatkowych kodów CSS i JavaScript**: Zwrócony kod HTML powinien zawierać jedynie zawartość przeznaczoną do wstawienia pomiędzy tagi <body> i </body>. **Nie** dołączaj znaczników <html>, <head> ani <body>.
    4. **Dokładność**: NIE dodawaj na poczatku kodu: ```html oraz ``` na końcu w kodzie
    5. **Zmiany**: Nie Zmieniaj ani nie dodawaj treści do artykułu niżej.
    Artykuł:
    """

    article_content = read_article(article_path)
    html_content = generate_html(article_content, prompt)
    save_html_to_file(html_content, html_output_path)

if __name__ == '__main__':
    main()