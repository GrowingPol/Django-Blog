from django.urls import path
from . import views # . means current directory
from .views import PostListView
urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('about', views.about, name= 'blog-about'),
]
