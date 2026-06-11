from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api_root/Post', views.PostViewSet, basename='post')

urlpatterns = [
    # 1. 기존 웹 페이지용 주소 패턴들 (그대로 유지)
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('js/', views.js_test, name='js_test'),

    path('', include(router.urls)),
]