from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    functions = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.name} {self.functions}"
