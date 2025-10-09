from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work05/', include('work05.urls')),  # work05
    path('work06/', include('work06.urls')),  # work06
    path('work07/', include('work07.urls')),  # work07
    path('', include('work07.urls')),  # ルートURLでwork07アプリを表示
]
