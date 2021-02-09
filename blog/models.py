from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    date_created = models.DateField(default=timezone.now)
    author = models.CharField(max_length=60, blank=True)
    main_text = models.TextField(blank=True)
    is_hidden = models.BooleanField(default=False)
#   attached_file = models.FileField()

