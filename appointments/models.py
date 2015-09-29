"""
HealthNet Appointments models
"""

from django.db import models

class Appointment(models.Model):
    title = models.CharField(max_length=32)
    when = models.DateTimeField()
    patient = models.CharField(max_length=100)
    doctor = models.CharField(max_length=96)
    hospital = models.CharField(max_length=64)
    room = models.CharField(max_length=32)
    reason = models.TextField()

