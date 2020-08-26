from django.http import HttpResponse
from django.shortcuts import render

from .models import Event  # Import the model classes we just wrote.

def index(request):
    events = Event.objects.all()

    print(events[0].image)
    context = {'events': events}

    return render(request, 'ateliere.html', context)

def detaliu(request):
    return render(request, 'ateliere_detaliu.html', {})

def register(request, id):
    print(request.method)
    if (request.method == "GET") :
        return render(request, 'register.html', {})
    elif (request.method == "POST"):
        b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
        b.save()
        print(request.POST.get("nume", ""))
        print(request.POST.get("prenume", ""))
        print(request.POST.get("email", ""))
        print(request.POST.get("telefon", ""))

        return render(request, 'register.html', {})