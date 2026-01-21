from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('stock-in/<int:pk>/', views.stock_in, name='stock_in'),
    path('stock-out/<int:pk>/', views.stock_out, name='stock_out'),
    path('history/', views.history_list, name='history_list'),  
]
