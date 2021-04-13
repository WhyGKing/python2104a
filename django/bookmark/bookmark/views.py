from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List 뷰를 상속받아 리스트 뿌려주기 만들어보자
# 클래스형 뷰를 사용할거임...
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
# 웹페이지에 접속한다 => 페이지를 본다
# UL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다 -> 응답
# url과 연결시켜줘야 함...

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')     #대신에 get_absolute_url을 정의하여 사용하기도 함
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_confirm_delete'