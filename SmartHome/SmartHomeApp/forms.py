from django import forms
from SmartHomeApp.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['owner']

class FilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)
        self.end_date = kwargs.pop('end_date', None)
        self.start_date = kwargs.pop('start_date', None)
        self.device = kwargs.pop('device', None)
        super().__init__(*args, **kwargs)
        self.fields['start_date'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=False,
                                                    initial=self.start_date)
        self.fields['end_date'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False,
                                                  initial=self.end_date)
        self.fields['device'] = forms.ModelChoiceField(queryset=Device.objects.for_user(self.current_user),required=False,
                                                       initial=self.device)










