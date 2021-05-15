from django.contrib import admin

# Register your models here.

from .models import SummerSchoolEventAdmin
from .models import SummerSchoolEvent
from .models import SummerSchoolParticipation

admin.site.register(SummerSchoolEvent, SummerSchoolEventAdmin)
admin.site.register(SummerSchoolParticipation)
