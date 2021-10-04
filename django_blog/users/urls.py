from django.urls import path
from . import views # . means current directory
urlpatterns = [
    path('register', views.register, name='user-registration'),
    path('profile', views.profile, name='profile'),
]