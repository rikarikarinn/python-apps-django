from django.urls import path
from . import views

app_name = 'work10'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='create'),
    path('edit/<int:pk>/', views.todo_edit, name='edit'),
    path('delete/<int:pk>/', views.todo_delete, name='delete'),
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle'),
]
