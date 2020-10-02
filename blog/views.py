from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy

class BlogListView(ListView): #リスト
    model = Blog
    context_object_name = 'blogs'

class BlogDetailView(DetailView): #詳細ページ
    model = Blog
    context_object_name = 'blog'

class BlogCreateView(CreateView): #記事の作成
    model = Blog
    #fields = ['content'] #編集系ビューでは必ず定義する
    success_url = reverse_lazy("index") #トップページに遷移する
    form_class = BlogForm
    template_name = 'blog/blog_create_form.html'

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました')
        return super().form_invalid(form)

class BlogUpdateView(UpdateView): #更新
    model = Blog
    #fields = ['content']
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk':blog_pk})
        return url

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")
