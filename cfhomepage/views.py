from django.http import HttpResponse
from django.shortcuts import render
from .models import SocialProjects

def index(request):
    return render(request, 'homepage.html', {})

def rules(request):
    return render(request, 'reguli.html', {})

def covid(request):
    return render(request, 'covid.html', {})

def social_projects(request):
    socialProjects = SocialProjects.objects.all()

    return render(request, 'sociale.html', {"projects": socialProjects})