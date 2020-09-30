from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

class BlogListView(ListView): #リスト
    model = Blog

class BlogDetailView(DetailView): #詳細ページ
    model = Blog

class BlogCreateView(CreateView): #フォーム
    model = Blog
    fields = ['content'] #必ず定義する
    success_url = reverse_lazy("index") #トップページに遷移する
