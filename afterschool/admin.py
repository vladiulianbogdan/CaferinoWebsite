from django.contrib import admin

# Register your models here.

from .models import AfterSchoolEventAdmin
from .models import AfterSchoolEvent
from .models import AfterSchoolParticipation

admin.site.register(AfterSchoolEvent, AfterSchoolEventAdmin)
admin.site.register(AfterSchoolParticipation)
