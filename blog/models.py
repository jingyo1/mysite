from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 다른 모델(사용자)과의 연결을 의미합니다 (글쓴이)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 글자 수가 제한된 텍스트 (제목)
    title = models.CharField(max_length=200)
    # 글자 수 제한이 없는 긴 텍스트 (내용)
    text = models.TextField()
    # 날짜와 시간 (작성일 - 기본값은 현재 시간)
    created_date = models.DateTimeField(default=timezone.now)
    # 날짜와 시간 (게시일 - 빈칸 허용)
    published_date = models.DateTimeField(blank=True, null=True)

    # 게시하기 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 이 글의 제목을 그대로 반환해주는 함수
    def __str__(self):
        return self.title