from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shApp_start(request):
    return render(request, 'shAppStart.html')

def shApp(request):
    return render(request, 'shApp.html')
