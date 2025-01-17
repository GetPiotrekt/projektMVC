1. Informacje o projekcie

Projekt został stworzony wspólnie przeze mnie i znajomego z kierunku, z którym robiłem ten projekt. 
Zdecydowaliśmy się na użycie Django jako frameworka, ponieważ chcieliśmy przećwiczyć programowanie w Pythonie i lepiej zrozumieć działanie aplikacji webowych. 
Naszym celem było stworzenie jakże odkrywczej aplikacji do zarządzania listą zadań (To-Do List).

2. Wybór Django

Django to framework webowy napisany w Pythonie, który pozwala na szybkie tworzenie aplikacji przy zachowaniu dobrej organizacji kodu. 
Oferuje wiele gotowych funkcji, takich jak obsługa bazy danych, system szablonów czy panel administracyjny. 
Dzięki temu mogliśmy skupić się na samej logice aplikacji, zamiast pisać wszystko od zera.

Dodatkowo, do stylizacji aplikacji wykorzystaliśmy Bootstrap, co pozwoliło nam szybko stworzyć responsywny i estetyczny interfejs 
użytkownika bez potrzeby pisania własnych arkuszy CSS.

3. Konfiguracja projektu

W celu uruchomienia potrzeba:
  Python 3.6+
  pip (menedżer pakietów dla Pythona)
  virtualenv (opcjonalnie, ale korzystaliśmy z tego)

Jak uruchomić?:
  Po zainstalowaniu, trzeba uruchomić serwer za pomocą "python manage.py runserver"
  Po uruchomieniu wystarczy wejść w przeglądarce pod adres http://127.0.0.1:8000/
  Pierwsza wyświetli się strona umożliwiająca zarządzenie listą zadań

4. Struktura plików projektu - kluczowe foldery i pliki

projekt/
│── manage.py          # Główny plik do uruchamiania poleceń Django
│── taskmanager/
│   ├── settings.py    # Główne ustawienia aplikacji Django
│   ├── urls.py        # Definiowanie ścieżek URL
│   ├── wsgi.py        # Punkt wejściowy dla serwera WSGI
│
│── tasks/             # Aplikacja do zarządzania zadaniami
│   ├── models.py      # Definicja modelu Task (baza danych)
│   ├── views.py       # Logika widoków (obsługa żądań)
│   ├── urls.py        # Ścieżki URL dla aplikacji tasks
│   ├── forms.py       # Formularze do tworzenia i edycji zadań
│   ├── serializers.py # Serializery dla API REST
│   ├── templates/     # Pliki HTML dla aplikacji
│
│── db.sqlite3         # Lokalna baza danych SQLite

5. Django i wzorzec MVC

Django wykorzystuje wzorzec MVC (Model-View-Controller), ale w nieco zmienionej formie, którą nazywa MTV (Model-Template-View).
  Model (M - Models.py) – odpowiada za warstwę danych i definiuje strukturę bazy danych.
  View (V - Views.py) – odpowiada za logikę aplikacji, pobieranie danych i ich przetwarzanie.
  Template (T - Templates/) – odpowiada za warstwę prezentacji (HTML, css w formie Bootstrap).

A w Django to wygląda tak:
  models.py definiuje bazę danych
  views.py przetwarza żądania użytkownika i zwraca odpowiednie dane
  templates/ zawiera interfejs użytkownika

Przykładowy przepływ:
  1. Użytkownik wpisuje adres w przeglądarce.
  2. plik urls.py przekierowuje to zapytanie do odpowiedniego widoku (views.py).
  3. Widok pobiera dane z models.py i przekazuje je do templates/.
  4. Użytkownik widzi stronę z listą zadań.
  
6. Podsumowanie
Ten projekt to prosty system zarządzania zadaniami, który został stworzony z wykorzystaniem Django. Dzięki temu nauczyliśmy się:
  Jak działa Django i jego wzorzec MTV.
  Jak tworzyć i obsługiwać modele, widoki oraz szablony.
  Jak wdrażać REST API w Django.
  Jak używać Bootstrap do stylizacji aplikacji.
