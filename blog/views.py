from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')

    context = {'blog_posts': posts}
    return render(request, 'blog.html', context)

def detaliu(request, id):
    post = BlogPost.objects.get(id=id)

    return render(request, 'blog_detaliu.html', {'blog_post': post})
