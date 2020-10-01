from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

class BlogListView(ListView): #リスト
    model = Blog

class BlogDetailView(DetailView): #詳細ページ
    model = Blog

class BlogCreateView(CreateView): #記事の作成
    model = Blog
    #fields = ['content'] #編集系ビューでは必ず定義する
    success_url = reverse_lazy("index") #トップページに遷移する
    form_class = BlogForm

class BlogUpdateView(UpdateView): #更新
    model = Blog
    #fields = ['content']
    form_class = BlogForm

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk':blog_pk})
        return url

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")
