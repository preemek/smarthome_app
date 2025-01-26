from dataclasses import field
from datetime import datetime, timezone
from lib2to3.fixes.fix_input import context

from django.db.models import Sum, Subquery, F
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title

from SmartHomeApp.models import Device, LogRow
from SmartHomeApp.forms import DeviceForm
from django.contrib.auth.decorators import login_required

import plotly.express as px

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
        LogRow.objects.create(device=device, owner=request.user, power_in_watts=device.power_in_watts,
                              time_in_seconds=0)
    else:
        device.status = 0
        log_row = LogRow.objects.get(device=device, owner=request.user, time_in_seconds=0)
        log_row.off_timestamp = datetime.now(timezone.utc)
        log_row.time_in_seconds = (log_row.off_timestamp - log_row.on_timestamp).seconds
        log_row.save()
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

@login_required(login_url='login')
def shApp_logs(request):
    logs = LogRow.objects.filter(owner=request.user).order_by('on_timestamp').reverse()

    return render(request, 'shApp_logs.html', {"logs": logs})


@login_required(login_url='login')
def shApp_stats(request):
    logs = LogRow.objects.filter(owner=request.user
                                  ).annotate(total_power_utilisation
                                                         = F('power_in_watts') * F('time_in_seconds') / 3600)
    logs_sum_total_power = (logs.values('device__name')
             .order_by('device__name')
             .annotate(sum_power_utilisation=Sum('total_power_utilisation')))

    fig = px.bar(
        logs_sum_total_power,
        x = 'device__name',
        y = 'sum_power_utilisation',
        title = 'Power utilisation by device',
        labels = {'device__name':'device', 'sum_power_utilisation':'Wh'},
        color='device__name',
    )

    fig.update_layout(title = {'font_size': 20,'xanchor': 'center', 'x': 0.5})

    chart_sum_total_power = fig.to_html()
    return render(request, 'shApp_stats.html', {'chart_sum_total_power': chart_sum_total_power})




