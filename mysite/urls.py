from django.contrib import admin
from django.urls import path, include  # ✨ include를 꼭 추가하세요!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),    # ✨ 메인 주소로 오면 blog 앱의 주소록을 보라는 설정입니다.
]