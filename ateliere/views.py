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

    return render(request, 'ateliere_detaliu.html', {'event': event,'eventDates': event.eventdate_set.all()})

def register(request, id):
    event = Event.objects.get(id=id)

    if (request.method == "GET"):
        return render(request, 'register.html', {'event': event,'eventDates': event.eventdate_set.all()})
    elif (request.method == "POST"):
        b = Participation(event_id=event, name=request.POST.get("nume", "")  + " " + request.POST.get("prenume", ""), childName=request.POST.get('childName'), childAge=request.POST.get('childAge'), email=request.POST.get("email", ""), phone=request.POST.get("telefon", ""), date=request.POST.get("eventDate", ""))
        b.save()

        try:
            mailMessage = """
Buna! 

Ne bucuram ca doresti sa participi la atelierul nostru!
Am primit cererea ta de participare. Te vom contacta prin mail sau sms pentru a valida inscriere in cel mai scurt timp.
Acest e-mail este trimis automat de sistem si informeaza ca am primit inscrierea dvs, nu garanteaza ca mai sunt locuri disponibile. Disponibilitatea si confirmarea va fi transmisa ulterior in functie de numarul de copii deja inscrisi.

O zi minunata va dorim!
Echipa COFFERINO HUB
            """
            email = EmailMessage('Am primit cererea ta de participare la ' + event.title, mailMessage, to=[b.email])
            email.send()

            email = EmailMessage('Ai un nou participant la cursul ' + event.title, 'Ai un nou participant la cursul ' + event.title, to=["cofferino.hub@gmail.com"])
            email.send()
        except Exception as e:
            print(e)

        return render(request, 'register_confirmation.html', {})
