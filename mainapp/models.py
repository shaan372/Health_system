from django.db import models

# Create your models here.

class Readings(models.Model):

    temp = models.FloatField(default="300.0")
    pulse = models.FloatField(default="133.0")
    date = models.DateField()
    time = models.TimeField()

