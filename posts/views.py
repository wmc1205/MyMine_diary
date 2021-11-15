


#제목 리스트
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from posts.form import PostForm
from posts.models import Post


def index(request):
    post_list = Post.object.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html',context)


#내용 상세 페이지
class createView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'posts/create.html'
