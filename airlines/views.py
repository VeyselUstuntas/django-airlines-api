from django.shortcuts import get_object_or_404, redirect, render
from .models import Airline, Aircraft

from rest_framework import generics
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from rest_framework.permissions import IsAuthenticated

class AirlineListCreateView(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    #permission_classes = [IsAuthenticated]

class AirlineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    #permission_classes = [IsAuthenticated]

class AircraftListCreateView(generics.ListCreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    #permission_classes = [IsAuthenticated]

class AircraftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    #permission_classes = [IsAuthenticated]

def airline_list(request):
    airlines = Airline.objects.all()
    return render(request, 'airlines/airline_list.html', {'airlines': airlines})

def aircraft_list(request):
    aircrafts = Aircraft.objects.all()
    return render(request, 'airlines/aircraft_list.html', {'aircrafts': aircrafts})


def airline_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        callsign = request.POST["callsign"]
        base_airport = request.POST["base_air"]
        founded_year = request.POST["founded_year"]

        new_airline = Airline(name=name,callsign=callsign,base_airport = base_airport,founded_year = founded_year)
        new_airline.save()
    return render(request,'airlines/airline_create.html')


def aircraft_create(request):
    if request.method == "POST":
        serial_number = request.POST["serial_number"]
        type = request.POST["type"]
        model = request.POST["model"]
        engine = request.POST["engine"]
        op_airline = Airline.objects.get(id = request.POST["op_airline"])

        new_aircraft = Aircraft(manufacturer_serial_number = serial_number, type = type, model = model, number_of_engines = engine, operator_airline = op_airline)

        new_aircraft.save()


    return render(request,'airlines/aircraft_create.html')


def airline_delete(request, id):
    airline = get_object_or_404(Airline, id = id)
    if request.method == "POST":
        airline.delete()
        return redirect("airline-list")

    return render(request, "airlines/airline_delete.html", {"airline":airline})

def aircraft_delete(request):
    pass

def airline_edit(request,id):
    airline = get_object_or_404(Airline, id = id)

    if request.method == "POST":
        name = request.POST["name"]
        callsign = request.POST["callsign"]
        base_airport = request.POST["base_air"]
        founded_year = request.POST["founded_year"]

        new_airline = Airline(id = id ,name=name,callsign=callsign,base_airport = base_airport,founded_year = founded_year)
        new_airline.save()
        return redirect("airline-list")

    return render(request, "airlines/airline_edit.html", {"airline":airline})

def aircraft_edit(request):
    pass
