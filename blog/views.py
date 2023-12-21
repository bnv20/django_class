from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# CBV: Class Based View
class PostList(ListView):
    model = Post
    ordering = "-pk"
    

class PostDetail(DetailView):
    model = Post
   




# FBV: Function Based View
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 모든 Post 객체를 가져와서 pk 역순으로 정렬

#     return render( # render 함수는 세 번째 인수로 전달된 딕셔너리 데이터를 템플릿 파일에 적용하여 HTML 코드로 변환
#         request, # 첫 번째 인수는 반드시 request
#         'blog/index.html', # 두 번째 인수는 템플릿 파일의 경로
#         {
#             'posts': posts, # posts 키에 posts 변수를 할당
#         }
#     )

# def single_post_page(request, pk): # pk는 URL에서 추출한 게시물의 고유 번호
#     post = Post.objects.get(pk=pk) # pk가 매개변수 pk와 같은 Post 객체를 post 변수에 할당

#     return render(
#         request,
#         'blog/single_post_page.html', # 템플릿 파일의 경로
#         {
#             'post': post,
#         }
#     )
