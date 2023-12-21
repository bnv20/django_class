import os
from django.db import models

class Post(models.Model): # Post 모델 정의
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)

    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add: 생성 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now: 수정 시간을 자동으로 저장
    # author: 추후 작성 예정

    def __str__(self): # 객체를 문자열로 표현할 때 사용
        return f'[{self.pk}]{self.title}' # pk: 객체의 고유한 번호, title: 제목. 게시물의 기본 키가 대괄호로 묶인 문자열을 출력하고 바로 뒤에 게시물 제목이 표시
    def get_absolute_url(self): # get_absolute_url 메서드 정의
        return f'/blog/{self.pk}/' # 게시물의 상세 페이지 주소를 반환
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split(".")[-1]