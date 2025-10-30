from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # ← 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work05/', include('work05.urls')),
    path('work06/', include('work06.urls')),
    path('work07/', include('work07.urls')),
    path('work08/', include('work08.urls')),
    path('work09/', include('work09.urls')), 
    path('work10/', include('work10.urls')), 
    path('sns/', include('sns.urls')),

    # 🔹 ログイン・ログアウト
    path('login/', auth_views.LoginView.as_view(template_name='work10/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

# 開発中のみメディアファイルを配信
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
