from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView


def home(request):
    if request.method == "POST":
        return render(request, 'accounts/home.html', context={'text' : 'POST METHOD!!!'})
    else :
        return render(request, 'accounts/home.html', context={'text' : 'GET METHOD!!!'})

class AccountCreateView(CreateView):
    model = User
    form_class =UserCreationForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'tUser'
    template_name = 'accounts/detail.html'