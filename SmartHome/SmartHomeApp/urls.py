from django.urls import path
from SmartHomeApp.views import shApp_start

urlpatterns = [
    path('start/', shApp_start, name='start'),
]