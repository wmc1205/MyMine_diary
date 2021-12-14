from django.urls import path

from . import views
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'posts'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',PostDeleteView.as_view(), name='delete'),
    ]