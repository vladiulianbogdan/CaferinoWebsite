from django.http import HttpResponse
from django.shortcuts import render

from .models import Event
from .models import Participation
from django.core.mail import EmailMessage

def index(request):
    events = Event.objects.all().order_by('-start_date')

    context = {'events': events}

    return render(request, 'ateliere.html', context)

def detaliu(request, id):
    event = Event.objects.get(id=id)

    return render(request, 'ateliere_detaliu.html', {'event': event})

def register(request, id):
    event = Event.objects.get(id=id)

    if (request.method == "GET"):
        return render(request, 'register.html', {'event': event})
    elif (request.method == "POST"):
        b = Participation(event_id=event, name=request.POST.get("nume", "")  + " " + request.POST.get("prenume", ""), email=request.POST.get("email", ""), phone=request.POST.get("telefon", ""))
        b.save()

        try:
            email = EmailMessage('Iti confirmam inscrierea la evenimentul ' + event.title, 'Iti confirmam inscrierea la evenimentul ' + event.title, to=[b.email])
            email.send()

            email = EmailMessage('Ai un nou participant la cursul ' + event.title, 'Ai un nou participant la cursul ' + event.title, to=["mirela@caferino.ro"])
            email.send()
        except Exception as e:
            print(e)

        return render(request, 'register_confirmation.html', {})
