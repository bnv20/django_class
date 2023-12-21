from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page), # pk가 정수형임을 명시
    # path('', views.index), # 블로그 메인 페이지
    path("<int:pk>/", views.PostDetail.as_view()),
    path("", views.PostList.as_view()),
]