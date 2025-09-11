from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),         # work05/ にアクセスしたとき
    path('index/', views.index, name='index'),  # work05/index/
    path('list/', views.list, name='list'),    # work05/list/
]
