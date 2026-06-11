from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

# 라우터 객체 생성 및 안드로이드 API 주소 등록
router = DefaultRouter()
router.register(r'api/post', views.PostViewSet, basename='post')

urlpatterns = [
    # 1. 기존 웹 페이지용 주소 패턴들 (그대로 유지)
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('js/', views.js_test, name='js_test'),
    
    # 2. 🌟 안드로이드 앱이 호출할 API 주소를 장고 주소판에 합쳐줍니다.
    path('', include(router.urls)), 
]