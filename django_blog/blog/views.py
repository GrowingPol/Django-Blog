from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
posts = [
    {
        'author': 'GrowingPol',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'September 27, 2021'
    },
    {
        'author': 'Mary Ann',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'September 28, 2021'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'The About Page'})