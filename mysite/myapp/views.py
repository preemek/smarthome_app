
from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.http import JsonResponse
import json
from .mqtt_client import client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

def devices_list(request):
    devices = Device.objects.all()  
    return render(request, 'devices_list.html', {'devices_list': devices})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('/')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('devices_list')  
    else:
        form = DeviceForm()  

    return render(request, 'add_device.html', {'form': form})

def delete_device(request, pk):
    if request.method == 'POST':
        device = get_object_or_404(Device, pk=pk)
        device.delete()
        return JsonResponse({'succes': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status = 400)

def toggle_device_status(request, device_id):
    
    device = Device.objects.get(id=device_id)
    new_status = not device.status
    device.status = new_status
    device.save()

    topic = f"devices/{device_id}/control"
    payload = "ON" if new_status else "OFF"
    client.publish(topic, payload)

    return JsonResponse({"success": True, "new_status": new_status})
 

