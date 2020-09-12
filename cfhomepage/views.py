from django.http import HttpResponse
from django.shortcuts import render
from .models import SocialProjects
from .models import Banner

def index(request):
    banners = Banner.objects.all()  

    return render(request, 'homepage.html', {"banners": banners})

def rules(request):
    return render(request, 'reguli.html', {})

def gdpr(request):
    return render(request, 'gdpr.html', {})

def covid(request):
    return render(request, 'covid.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def club(request):
    return render(request, 'newsletter.html', {})


def social_projects(request):
    socialProjects = SocialProjects.objects.all()

    return render(request, 'sociale.html', {"projects": socialProjects})