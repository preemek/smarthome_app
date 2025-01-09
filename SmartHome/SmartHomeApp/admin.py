from django.contrib import admin
from SmartHomeApp.models import Device

# Register your models here.
#admin.site.register(Device)
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "owner"]
    list_filter = ["owner"]
    search_fields = ["name", "description"]