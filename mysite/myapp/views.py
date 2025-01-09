from django.shortcuts import render, redirect
from .models import Device
from .forms import DeviceForm
# Create your views here.

def devices_list(request):
    devices = Device.objects.all()
    return render(request, 'device/devices_list.html', {'devices': devices})

def home(request):
    return render(request, 'home.html')

def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devices_list')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})