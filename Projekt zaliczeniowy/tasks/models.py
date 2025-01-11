from django.db import models  # Importujemy moduł do definiowania modeli w Django

# Definicja modelu Task (to nasza "tabela" w bazie danych)
class Task(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    # Metoda, która zwraca czytelną nazwę zadania w formie tekstu
    def __str__(self):
        return self.title
