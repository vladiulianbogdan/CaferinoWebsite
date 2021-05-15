from django.http import HttpResponse
from django.shortcuts import render

from .models import SummerSchoolEvent
from .models import SummerSchoolParticipation
from django.core.mail import EmailMessage

def index(request):
    events = SummerSchoolEvent.objects.all().order_by('-start_date')

    context = {'events': events}

    return render(request, 'summer-school.html', context)

def detaliu(request, id):
    event = SummerSchoolEvent.objects.get(id=id)

    return render(request, 'summer-school-details.html', {'event': event})

def register(request, id):
    event = SummerSchoolEvent.objects.get(id=id)

    if (request.method == "GET"):
        return render(request, 'summers_school_register.html', {'event': event})
    elif (request.method == "POST"):
        b = SummerSchoolParticipation(event_id=event, name=request.POST.get("nume", "")  + " " + request.POST.get("prenume", ""), childName=request.POST.get('childName'), childAge=request.POST.get('childAge'), email=request.POST.get("email", ""), phone=request.POST.get("telefon", ""))
        b.save()

        try:
            email = EmailMessage('Iti confirmam inscrierea la evenimentul ' + event.title, 'Iti confirmam inscrierea la evenimentul ' + event.title, to=[b.email])
            email.send()

            email = EmailMessage('Ai un nou participant la cursul ' + event.title, 'Ai un nou participant la cursul ' + event.title, to=["cofferino.hub@gmail.com"])
            email.send()
        except Exception as e:
            print(e)

        return render(request, 'summers_school_register_confirmation.html', {})
