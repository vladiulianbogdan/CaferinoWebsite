from django.contrib import admin

# Register your models here.
from .models import SocialProjects
from .models import Banner

admin.site.register(SocialProjects)
admin.site.register(Banner)