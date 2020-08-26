from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost  # Import the model classes we just wrote.


# Create your views here.
def index(request):
    posts = BlogPost.objects.all()

    print(posts)
    context = {'blog_posts': posts}
    return render(request, 'blog.html', context)

def detaliu(request, id):
    post = BlogPost.objects.get(id=id)

    return render(request, 'blog_detaliu.html', {'blog_post': post})
