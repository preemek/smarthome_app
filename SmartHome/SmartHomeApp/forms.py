import django.contrib.auth.models
from django import forms
from django.contrib.auth import authenticate

from SmartHomeApp.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['owner']

class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)
        cu = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        self.fields['device'] = forms.ModelChoiceField(queryset=Device.objects.for_user(self.current_user))


    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
