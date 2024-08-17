from django.shortcuts import render
from .models import Airline, Aircraft

def airline_list(request):
    airlines = Airline.objects.all()
    return render(request, 'airlines/airline_list.html', {'airlines': airlines})

def aircraft_list(request):
    aircrafts = Aircraft.objects.all()
    return render(request, 'airlines/aircraft_list.html', {'aircrafts': aircrafts})
