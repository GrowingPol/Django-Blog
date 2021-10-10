from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default is <app>/<model>_<viewtype>.html
    context_object_name =  'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView): #LoginRequiredMixin avoid to access this view without logging in
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user #set author for the post
        return super().form_valid(form)

def about(request):
    return render(request,'blog/about.html',{'title':'The About Page'})