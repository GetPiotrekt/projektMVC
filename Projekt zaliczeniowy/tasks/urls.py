from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Strona główna
    path('add/', views.add_task, name='add_task'), # Strona dodawania
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), # Strona edytowania
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), # Strona usuwania
    path('api/', views.task_list_api, name='task_list_api'), # Strona która pokazuje zapis rest api
]
