from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task  # Nasz model, który ogarnia zadania
from .forms import TaskForm  # Formularz do dodawania i edytowania zadań
from rest_framework.decorators import api_view  # Potrzebne, żeby stworzyć API
from rest_framework.response import Response  # Żeby zwracać dane w formacie JSON
from .serializers import TaskSerializer  # Zamiana obiektów Task na JSON, żeby API wiedziało, co zwrócić

# API: Zwraca listę wszystkich zadań w formie JSON (ładnie widać co się zapisuje)
@api_view(['GET'])
def task_list_api(request):
    tasks = Task.objects.all()  # Wyciągamy wszystkie zadania z bazy
    serializer = TaskSerializer(tasks, many=True)  # Przerabiamy je na JSON
    return Response(serializer.data)  # I zwracamy w odpowiedzi

# Główna strona: Lista zadań z opcją filtrowania
def task_list(request):
    filter_option = request.GET.get('filter', 'all')  # Sprawdzamy, czy użytkownik coś chce filtrować
    
    # Filtrowanie po statusie zadania
    if filter_option == 'completed':
        tasks = Task.objects.filter(completed=True)  # Wyciągamy te wykonane
    elif filter_option == 'pending':
        tasks = Task.objects.filter(completed=False)  # Wyciągamy te, które jeszcze trzeba zrobić
    else:
        tasks = Task.objects.all()  # A jak nie, to dajemy wszystko
    
    # Ładujemy listę zadań na stronę
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter': filter_option})

# Taka testowa stronka
def index(request):
    return HttpResponse("W końcu działa!")

# Dodawanie nowego zadania
def add_task(request):
    if request.method == 'POST':  # Jak użytkownik kliknął "Dodaj"
        form = TaskForm(request.POST)  # Zbieramy dane z formularza
        if form.is_valid():  # Sprawdzamy, czy wszystko OK
            form.save()  # Zapisujemy zadanie do bazy
            return redirect('task_list')  # Wracamy na stronę z listą zadań
    else:  # Jak otworzył formularz, a nie kliknął
        form = TaskForm()  # Dajemy pusty formularz
    return render(request, 'tasks/add_task.html', {'form': form})  # Ładujemy formularz na stronę

# Edycja istniejącego zadania
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Łapiemy zadanie z bazy na podstawie ID
    if request.method == 'POST':  # Jak kliknął "Zapisz zmiany"
        form = TaskForm(request.POST, instance=task)  # Podpinamy dane zadania
        if form.is_valid():  # Jak wszystko OK
            form.save()  # Zapisujemy zmiany
            return redirect('task_list')  # Wracamy na listę zadań
    else:  # Jak dopiero otwiera formularz
        form = TaskForm(instance=task)  # Pokazujemy dane tego zadania w formularzu
    return render(request, 'tasks/edit_task.html', {'form': form})  # Wyświetlamy formularz

# Usuwanie zadania
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Łapiemy zadanie z bazy
    task.delete()  # Usuwamy je
    return redirect('task_list')  # Wracamy na listę zadań
