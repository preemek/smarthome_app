from django.contrib import admin
from SmartHomeApp.models import Device, LogRow

# Register your models here.
#admin.site.register(Device)
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "owner"]
    list_filter = ["owner"]
    search_fields = ["name", "description"]

@admin.register(LogRow)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["on_timestamp", "device", "owner", "power_in_watts", "off_timestamp", "time_in_seconds"]
    list_filter = ["owner"]
    search_fields = ["device", "owner"]