from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.decorators import accounts_ownership_required
from accounts.forms import AccountUpdateForm

#decorator's list
has_ownership = [login_required,accounts_ownership_required]

@login_required
def home(request):
    #logout 시 home 화면이 아닌 login 페이지로 rendering
    if request.method == "POST":
        return render(request, 'accounts/home.html', context={'text' : 'POST METHOD!!!'})
    else :
        return render(request, 'accounts/home.html', context={'text' : 'GET METHOD!!!'})

#회원가입
class AccountCreateView(CreateView):
    model = User
    form_class =UserCreationForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'tUser'
    template_name = 'accounts/detail.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'tUser'
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/update.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'tUser'
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/delete.html'