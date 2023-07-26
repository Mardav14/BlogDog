from django.shortcuts import render, HttpResponse
from home.models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()[:5]
    data = {
        'blogs' : blogs
    }
    return render(request, 'home.html', data)

def blog(request, url):
    blog = Blog.objects.get(url=url)
    data = {
        'blog' : blog
    }
    return render(request, 'blog.html', data )
