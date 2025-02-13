
from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.http import JsonResponse
from .mqtt_client import client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Eventlog
from django.utils.timezone import now


# Create your views here.
@login_required
def devices_list(request):
    devices = Device.objects.filter(user=request.user)  
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

@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save() 
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
 

def toggle_device_status(request, device_id):
    if request.method == "POST":
        device = get_object_or_404(Device, id=device_id)
        device.status = not device.status
        device.save()

        Eventlog.objects.create(
            user=request.user,
            device=device,
            action=f"Changed status to {'ON' if device.status else 'OFF'}",
            timestamp=now()
        )

        return JsonResponse({'success': True, 'new_status': device.status})
    return JsonResponse({'success': False}, status=400)

@login_required
def event_log(request):
    logs = Eventlog.objects.order_by('-timestamp')[:50]  
    print(logs)  
    return render(request, 'event_log.html', {'logs': logs})

