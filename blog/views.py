from django.shortcuts import render
from .models import BlogPost

def index(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blogposts': blogposts})

def blogpost(request, id):
    blogpost = BlogPost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html' , {'blogpost': blogpost})

def blogposts(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/blogpost.html', {'blogposts': blogposts})