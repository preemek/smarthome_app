from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=[('light', 'Light'), ('sensor', 'Sensor'), ('device', 'Device')])

    def __str__(self):
        return f"{self.name} ({self.topic})"
