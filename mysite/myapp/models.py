from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    functions = models.TextField(blank=True, null=True)  
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Eventlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device = models.ForeignKey('Device', on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.action} - {self.timestamp}'
    