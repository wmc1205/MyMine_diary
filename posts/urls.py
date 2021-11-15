from django.urls import path

from . import views
from .views import createView

app_name = 'posts'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('create/', createView.as_view(), name='create'),

]