from django.shortcuts import render, redirect, get_object_or_404
from SmartHomeApp.models import Device
from SmartHomeApp.forms import DeviceForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def shApp(request):
    return render(request, 'shApp.html')

@login_required(login_url='login')
def shApp_devices(request):
    devices = Device.objects.for_user(request.user)
    return render(request, 'shApp_devices.html', {"devices": devices})

@login_required(login_url='login')
def shApp_new_device(request):
    form = DeviceForm(request.POST or None)

    if form.is_valid():
        device = form.save(commit=False)
        device.owner = request.user
        device.save()
        return redirect('devices')
    else:
        return render(request, 'shApp_device_form.html', {'form': form, 'IsNew': True})

@login_required(login_url='login')
def shApp_edit_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    form = DeviceForm(request.POST or None, instance=device)

    if form.is_valid():
        device = form.save(commit=False)
        device.owner = request.user
        device.save()
        return redirect('devices')
    else:
        return render(request, 'shApp_device_form.html', {'form': form, 'IsNew': False})

@login_required(login_url='login')
def shApp_edit_OnOff(request, pk):
    device = get_object_or_404(Device, pk=pk)

    device.owner = request.user
    if device.status == 0:
        device.status = 1
    else:
        device.status = 0
    device.save()
    return redirect('devices')

@login_required(login_url='login')
def shApp_delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == 'POST':
        device.delete()
        return redirect('devices')
    else:
        return render(request, 'shApp_confirm_delete_device_form.html', {'device': device})




