from django.db import models
from django.contrib import admin
from datetime import datetime    
from django.utils.html import format_html

# Create your models here.
# Create your models here.
class Event(models.Model):
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
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)

    def publish_url(self):
        return "http://caferino.com/ateliere/register/" + str(self.id)
    
    def show_participants(self):
        participations = self.participation_set.all()

        print(participations)

        string = "<ul>"

        for participation in participations:
            string += "<li><a href='http://127.0.0.1:8000/admin/ateliere/participation/" + str(participation.id) +  "/change/'> " + participation.name + " " + participation.email + "</a></li>"

        string += "</ul>"

        return format_html(string)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'start_date', 'end_date', 'publish_url')
    readonly_fields = ['publish_url', 'show_participants']

    fieldsets = (
        (None, {
            'fields': ['title', 'image', "image1", "image2", "image3", "image4", "image5", "image6", 'content', 'start_date', 'end_date', 'category', 'price', ]
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
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)