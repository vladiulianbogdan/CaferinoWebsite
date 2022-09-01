from django.db import models
from django.contrib import admin
from datetime import datetime    
from django.utils.html import format_html

class EventManager(models.Manager):
    pass

# Create your models here.
# Create your models here.
class Event(models.Model):
    class Location(models.TextChoices):
        PARCUL_CIRCULUI = "Parcul Circului"
        AUREL_VLAICU = "Aurel Vlaicu"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'static/', help_text="Recommended image size: 324x175.")
    image1 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    image2 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    image3 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    image4 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    image5 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    image6 = models.ImageField(upload_to = 'static/', default="", blank=True, help_text="Recommended image size: 324x175.")
    category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=20, choices=Location.choices, default=Location.PARCUL_CIRCULUI)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    objects = EventManager()

    def publish_url(self):
        return "http://caferino.com/ateliere/register/" + str(self.id)
    
    def show_participants(self):
        participations = self.participation_set.all()

        string = "<ul>"

        for participation in participations:
            string += "<li><a href='/admin/ateliere/participation/" + str(participation.id) +  "/change/'> " + participation.name + ", " + participation.email + ", " + participation.phone + ", Nume copil:" + participation.childName + ", Varsta copil " + participation.childAge + "; Data participare: "+ participation.date + "</a></li></br>"

        string += "</ul>"

        return format_html(string)


class EventDate(models.Model):
    start_date = models.CharField(max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

class EventDateInLine(admin.TabularInline):
    model = EventDate 
    extra = 0

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'start_date', 'end_date', 'location', 'publish_url', '_eventDates')
    readonly_fields = ['publish_url', 'show_participants']

    inlines = [
       EventDateInLine 
    ]
 
    def _eventDates(self, obj):
        return obj.eventdate_set.all().count()

    fieldsets = (
        (None, {
            'fields': ['title', 'image', "image1", "image2", "image3", "image4", "image5", "image6", 'location', 'content', 'start_date', 'end_date', 'category', 'price', ]
        }),
        ('Advanced options', {
            'classes': ('collapse'),
            'fields': ['publish_url', "show_participants"],
        }),
    )

class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    childName = models.CharField(max_length=200)
    childAge = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default="")
