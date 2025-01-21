from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs = {'placeholder':"Input device's name"}),
            'function':forms.TextInput(attrs = {'placeholder':"Input device's function"}),      
                   }