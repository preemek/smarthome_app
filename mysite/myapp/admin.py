from django.contrib import admin
from .models import Device

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'type')
    search_fields = ('name', 'topic')
