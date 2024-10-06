from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class HealthInputs(models.Model):
    heartrate = models.CharField(max_length=255, blank=False)
    blood_pressure = models.CharField(max_length=255, blank=False)
    Temperature = models.CharField(max_length=255, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
















