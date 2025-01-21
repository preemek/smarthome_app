
from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.http import JsonResponse

# Create your views here.

def devices_list(request):
    devices = Device.objects.all()
    return render(request, 'myapp/devices_list.html', {'devices_list': devices})

def home(request):
    return render(request, 'home.html')

def add_device(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        functions = request.POST.get('functions')
        device = Device(name=name, functions=functions)
        device.save()
        return redirect('devices_list')  
    return render(request, 'add_device.html')

def delete_device(request, pk):
    if request.method == 'POST':
        device = get_object_or_404(Device, pk=pk)
        device.delete()
        return JsonResponse({'succes': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status = 400)


 

