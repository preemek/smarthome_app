from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class DeviceManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Device(models.Model):
    STATUS_CHOICES = (
        (0, 'Off'), (1, 'On')
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    status = models.PositiveSmallIntegerField(null=False, blank=False, default=0, choices=STATUS_CHOICES)
    power_in_watts = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, default='no description')

    objects = DeviceManager()

    def __str__(self):
        return self.name