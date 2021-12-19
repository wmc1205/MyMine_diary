from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from posts.decorators import posts_ownership_required
from posts.form import PostForm
from posts.models import Post

#decorator's list
has_ownership = [login_required,posts_ownership_required]

# 제목 리스트
class PostIndexView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/index.html'
    paginate_by = 5



# 내용 상세 페이지
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'tPost'
    template_name = 'posts/detail.html'



# 새로운 글 등록
@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk':self.object.pk})

#내용 수정 페이지
@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    context_object_name = 'tPost'

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk':self.object.pk})

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    context_object_name = 'tPost'
    success_url = reverse_lazy('posts:index')