# work06/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='work06_top'),
    path('index/', views.index, name='work06_index'),
    path('reiwa/', views.reiwa, name='work06_reiwa'),
]
