from django.http import HttpResponse
from django.shortcuts import render

from .models import Event
from .models import Participation

def index(request):
    events = Event.objects.all()

    print(events[0].image)
    context = {'events': events}

    return render(request, 'ateliere.html', context)

def detaliu(request, id):
    event = Event.objects.get(id=id)

    return render(request, 'ateliere_detaliu.html', {'event': event})

def register(request, id):
    event = Event.objects.get(id=id)

    print(request.method)
    if (request.method == "GET"):
        return render(request, 'register.html', {'event': event})
    elif (request.method == "POST"):
        b = Participation(event_id=event, name=request.POST.get("nume", "")  + " " + request.POST.get("prenume", ""), email=request.POST.get("email", ""), phone=request.POST.get("telefon", ""))
        b.save()

        return render(request, 'register.html', {})