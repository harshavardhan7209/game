from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    heading = models.CharField(max_length=400)
    body = models.TextField(max_length=100000000000000000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    