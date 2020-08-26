from django.contrib import admin

# Register your models here.

from .models import EventAdmin
from .models import Event
from .models import Participation

admin.site.register(Event, EventAdmin)
admin.site.register(Participation)