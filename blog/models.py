from django.db import models
from datetime import datetime    

# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'static/', help_text="Recommended image size: 324x175.")
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)