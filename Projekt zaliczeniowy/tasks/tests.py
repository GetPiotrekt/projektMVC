from django.test import TestCase  # Import klasy TestCase, żeby robić testy
from .models import Task  # Import naszego modelu Task

# Klasa do testów modelu Task
class TaskTestCase(TestCase):
    # Test, który sprawdza, czy zadanie można poprawnie stworzyć
    def test_task_creation(self):
        # Tworzymy nowe zadanie w bazie
        task = Task.objects.create(title="Test Task")
        # Sprawdzamy, czy tytuł zadania został poprawnie zapisany
        self.assertEqual(task.title, "Test Task")

# Aby odpalić trzeba wpisać: python manage.py test / py manage.py test

