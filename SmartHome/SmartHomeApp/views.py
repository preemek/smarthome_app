from datetime import datetime, timezone
from django.db.models import Sum, Subquery, F, Count
from django.shortcuts import render, redirect, get_object_or_404
from SmartHomeApp.models import Device, LogRow
from SmartHomeApp.forms import DeviceForm, FilterForm
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

def create_chart_sum_total_power_by_date(logs):
    logs_sum_total_power_by_date = (logs.values('off_timestamp__date')
                                    .order_by('off_timestamp__date')
                                    .annotate(sum_power_utilisation=Sum('total_power_utilisation')))

    fig_sum_total_power_by_date = px.line(
        logs_sum_total_power_by_date,
        x = 'off_timestamp__date',
        y = 'sum_power_utilisation',
        markers = True,
        title = 'Total power utilisation',
        labels = {'off_timestamp__date':'date', 'sum_power_utilisation':'Wh'},
    )

    fig_sum_total_power_by_date.update_layout(title={'font_size': 20, 'xanchor': 'center', 'x': 0.5})

    return fig_sum_total_power_by_date.to_html()

def create_chart_sum_total_power_by_device(logs):
    logs_sum_total_power_by_device = (logs.values('device__name')
                                      .order_by('device__name')
                                      .annotate(sum_power_utilisation=Sum('total_power_utilisation')))

    fig_sum_total_power_by_device = px.pie(
        logs_sum_total_power_by_device,
        names='device__name',
        values='sum_power_utilisation',
        title='Power utilisation by device',
        labels={'device__name': 'device', 'sum_power_utilisation': 'Wh'},
        color='device__name',
    )

    fig_sum_total_power_by_device.update_layout(title={'font_size': 20, 'xanchor': 'center', 'x': 0.5})

    return fig_sum_total_power_by_device.to_html()

def create_chart_count_on_off(logs):
    logs_count_on_off = (logs.values('device__name')
                         .order_by('device__name')
                         .annotate(count_on_off=Count('device__name')))

    fig_count_on_off = px.bar(
        logs_count_on_off,
        x='device__name',
        y='count_on_off',
        title='Number of times the device was switched on',
        labels={'device__name': 'device', 'count_on_off': 'number'},
        color='device__name',
    )

    fig_count_on_off.update_layout(title={'font_size': 20, 'xanchor': 'center', 'x': 0.5})

    return fig_count_on_off.to_html()


@login_required(login_url='login')
def shApp_stats(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    filter_devices = request.POST.get('device')

    logs = LogRow.objects.filter(owner=request.user
                                  ).annotate(total_power_utilisation
                                                         = F('power_in_watts') * F('time_in_seconds') / 3600)
    if start_date:
        logs = logs.filter(on_timestamp__gte=start_date)
    else:
        start_date = None
    if end_date:
        logs = logs.filter(on_timestamp__lte=end_date)
    else:
        end_date = datetime.now()
    if filter_devices:
        logs = logs.filter(device=filter_devices)

    filter_form = FilterForm(current_user=request.user, end_date = end_date, start_date = start_date, device = filter_devices)

    chart_sum_total_power_by_date = create_chart_sum_total_power_by_date(logs)
    chart_sum_total_power_by_device = create_chart_sum_total_power_by_device(logs)
    chart_count_on_off = create_chart_count_on_off(logs)

    return render(request, 'shApp_stats.html',
                  {'chart_sum_total_power': chart_sum_total_power_by_device
                      , 'chart_count_on_off': chart_count_on_off
                      , 'chart_sum_total_power_by_date': chart_sum_total_power_by_date
                      ,'form': filter_form})





