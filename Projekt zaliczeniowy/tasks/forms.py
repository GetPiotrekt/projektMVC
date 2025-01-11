from django import forms  # Importujemy moduł do obsługi formularzy
from .models import Task  # Importujemy nasz model Task, który będziemy wykorzystywać

# Formularz dla modelu Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Powiązanie formularza z modelem Task
        fields = ['title', 'description', 'completed']  # Pola, które będą widoczne w formularzu
