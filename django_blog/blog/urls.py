from django.urls import path
from . import views # . means current directory
from .views import (
    PostListView,
    PostDetailView,
    #PostCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post_detail'),
    #path('post/new/', PostCreateView.as_view(), name= 'post_create'), #it looks for <model>_form.html
    path('about', views.about, name= 'blog-about'),
]
