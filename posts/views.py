


#제목 리스트
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from posts.form import PostForm
from posts.models import Post

#제목 리스트
def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html',context)
# 내용 상세 페이지
def detail(request,post_id):

    post = get_object_or_404(Post, pk =post_id)
    return render(request,'posts/detail.html',{'post':post})

#새로운 글 등록
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = PostForm()
        return render(request,'posts/create.html', {'form':form})

