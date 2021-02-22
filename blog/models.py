from django.db import models
import datetime
from django.utils import timezone
import os
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    date_created = models.DateField(default=timezone.now)
    author = models.CharField(max_length=60, blank=True)
    main_text = models.TextField(blank=True)
    is_hidden = models.BooleanField(default=False)
    reference = models.ManyToManyField('Paper', related_name='contained_post', blank=True)
#   attached_file = models.FileField()
    def __str__(self):
        return self.title[:20]


def content_file_name(instance, filename):
    ext = filename.split('.')[-1] 
    filename = f'{instance.id}.{ext}'   
    return os.path.join('papers', filename)

class Paper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    journal = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=4, blank=True, default='')
    attachment = models.FileField(upload_to=content_file_name, blank=True)
    def __str__(self):
        return self.title
