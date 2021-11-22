
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from posts.form import PostForm
from posts.models import Post


# 제목 리스트
def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)


# 내용 상세 페이지
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request,'posts/detail.html', context)


# 새로운 글 등록
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/create.html', context)


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('posts:detail',pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'posts/update.html', context)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')
