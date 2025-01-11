from rest_framework import serializers  # Importujemy moduł do serializacji danych
from .models import Task  # Importujemy model Task z naszej aplikacji

# Definicja serializera dla modelu Task
class TaskSerializer(serializers.ModelSerializer):
    # To jest serializer, który konwertuje obiekty Task do formatu JSON (i odwrotnie).
    
    class Meta:
        # Wskazujemy, który model ma być serializowany
        model = Task  
        # Określamy, że chcemy serializować wszystkie pola z modelu Task
        fields = '__all__'
