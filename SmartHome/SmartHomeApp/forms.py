from django.forms import ModelForm
from SmartHomeApp.models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = ['owner']