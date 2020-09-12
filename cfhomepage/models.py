from django.db import models

# Create your models here.
class SocialProjects(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'static/')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    subtitle = models.CharField(max_length=200)
    description = models.TextField()

class Banner(models.Model):
    image = models.ImageField(upload_to = 'static/')
    url = models.CharField(max_length=200, default="#")