from django.db import models
from datetime import datetime

class Restaurant(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateField(default=datetime.now(), blank= True)
