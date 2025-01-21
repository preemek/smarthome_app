
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


 

