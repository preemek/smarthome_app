from django.urls import path
from SmartHomeApp.views import shApp_devices, shApp_new_device, shApp_edit_device, shApp_delete_device,shApp_edit_OnOff

urlpatterns = [
    path('devices/', shApp_devices, name='devices'),
    path('new_device/', shApp_new_device, name='new_device'),
    path('edit_device/<int:pk>/', shApp_edit_device, name='edit_device'),
    path('delete_device/<int:pk>/', shApp_delete_device, name='delete_device'),
    path('device_OnOff/<int:pk>/', shApp_edit_OnOff, name='device_OnOff'),
]