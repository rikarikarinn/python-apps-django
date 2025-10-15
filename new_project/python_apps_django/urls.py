from django.contrib import admin
from django.urls import path, include  # include を忘れずに
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work05/', include('work05.urls')),
    path('work06/', include('work06.urls')),
    path('work07/', include('work07.urls')),
    path('work08/', include('work08.urls')),
]

# 開発中のみメディアファイルを配信
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
