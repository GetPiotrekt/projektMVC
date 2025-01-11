from django.contrib import admin  # Importujemy moduł admin do rejestracji modeli w panelu administracyjnym
from .models import Task  # Importujemy nasz model Task

# Rejestrujemy model Task w panelu administracyjnym Django
admin.site.register(Task)  # Dzięki temu będziemy mogli zarządzać zadaniami z poziomu panelu admina
