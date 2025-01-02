from django.shortcuts import render
from .models import Device
# Create your views here.

def devices_list(request):
    devices = Device.objects.all()
    return render(request, 'device/devices_list.html', {'devices': devices})

def home(request):
    return render(request, 'home.html')