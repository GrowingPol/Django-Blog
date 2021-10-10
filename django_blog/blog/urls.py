from django.urls import path
from . import views # . means current directory
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name= 'user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post_detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name= 'post_delete'), #<model>_confirm_delete.html
    path('post/new/', PostCreateView.as_view(), name= 'post_create'), #it looks for <model>_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name= 'post_update'), #it looks for <model>_form.html
    path('about', views.about, name= 'blog-about'),
]
