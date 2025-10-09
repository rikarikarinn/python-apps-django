from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='work05_top'),
    path('index/', views.index, name='work05_index'),
    path('list/', views.list_view, name='work05_list'),
]
