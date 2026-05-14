from django.urls import path
from . import views  # 현재 폴더의 views.py를 가져옵니다.

urlpatterns = [
    path("", views.post_list, name="post_list"),  # 메인 주소('')로 접속하면 post_list 뷰를 실행하라는 뜻입니다.
]