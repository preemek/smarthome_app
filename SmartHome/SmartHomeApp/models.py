from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING


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
    description = models.CharField(max_length=300, null=True, blank=True, default='no description')


    objects = DeviceManager()

    def __str__(self):
        return self.name

class LogRow(models.Model):
    on_timestamp = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    power_in_watts = models.PositiveSmallIntegerField(null=False, blank=False)
    off_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    time_in_seconds = models.IntegerField(null=False, blank=False)


