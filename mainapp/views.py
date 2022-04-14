from django.shortcuts import render
from django.http import HttpResponse
from .models import Readings
from datetime import datetime
from datetime import date

# Create your views here.

def index(request):
    return HttpResponse('<h1>Index Page of the health system application</h1>')

def update(request):
    temp = request.GET.get('temp')
    pulse = request.GET['pulse']
    # date = datetime.now().strftime("%d/%m/%Y")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    print(date)
    print(time)
    print(temp)
    print(pulse)
    read = Readings(temp=temp, pulse=pulse, date=date, time=time)
    read.save()
    return HttpResponse("<h1>Done</h1>")
