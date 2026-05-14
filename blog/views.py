from django.shortcuts import render


# 메인 페이지 요청을 받으면 post_list.html 파일을 렌더링해서 보여줍니다.
def post_list(request):
    return render(request, "blog/post_list.html", {})