"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', views.devices_list, name='devices_list'),
    path('register/', views.register, name='register'),
    path('add_device/', views.add_device, name= 'add_device'),
    path('delete_device_ajax/<int:pk>/', views.delete_device, name= 'delete_device_ajax'),
    path('toggle_device_status/<int:device_id>/', views.toggle_device_status, name='toggle_device_status'),
    path('accounts/', include('accounts.urls')),  
    path('admin/', admin.site.urls),
    path('event_log/', views.event_log, name='event_log'),
    path('toggle_device_status/<int:device_id>/', views.toggle_device_status, name='toggle_device_status')
]
    
