from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accounts'
urlpatterns = [
    path('home/',views.home, name="home"),
    path('login/',LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('create/',AccountCreateView.as_view(),name="create"),
    path('detail/<int:pk>',AccountDetailView.as_view(),name="detail"),
    path('update/<int:pk>',AccountUpdateView.as_view(),name="update"),
    ]