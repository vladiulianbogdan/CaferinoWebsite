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
Bună! 

Ne bucurăm că doriți să participați la atelierul nostru! Am primit cererea dvs. de participare. 

Acest e-mail este trimis automat de sistem și vă informează că am primit înscrierea dvs, însă nu garantează că mai sunt locuri disponibile. Confirmarea va fi transmisă prin mail sau sms cu câteva zile înainte de atelier, în funcție de numărul copiilor deja înscriși și răspunsurile părinților acestora. 

Vă rugăm să răspundeți sms-ului de confirmare în termenul stabilit. In caz contrar vom considera că nu mai sunteți interesat de a participa la acest atelier, nu veți primi detaliile de plată și vom ceda locul următorului copil înscris. 

De asemenea, vă rugăm să nu achitați până nu primiți confirmarea prin sms de la noi, in cazul in care ați mai participat și aveți detaliile de plată. 

O zi minunată vă dorim!
Echipa COFFERINO HUB
            """
            email = EmailMessage('Am primit cererea ta de participare la ' + event.title, mailMessage, to=[b.email])
            email.send()

            email = EmailMessage('Ai un nou participant la cursul ' + event.title, 'Ai un nou participant la cursul ' + event.title, to=["cofferino.hub@gmail.com"])
            email.send()
        except Exception as e:
            print(e)

        return render(request, 'register_confirmation.html', {})
