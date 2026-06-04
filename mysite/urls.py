
from django.contrib import admin
from django.urls import path, include
from django.conf import settings               # ✨ 추가
from django.conf.urls.static import static     # ✨ 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# ✨ 정적 파일 및 미디어 파일의 URL 패턴을 프로젝트 주소에 더해줍니다.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)