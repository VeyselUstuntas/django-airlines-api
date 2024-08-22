from django.shortcuts import get_object_or_404, redirect, render
from .models import Airline, Aircraft
from rest_framework import generics
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required



# IsAuth JWT için açmayı unutma


# -------------------------------------API  methods 
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


# -------------------------------------list methods 
#@login_required
def airline_list(request):
    airlines = Airline.objects.all()
    return render(request, 'airlines/airline_list.html', {'airlines': airlines})

#@login_required
def aircraft_list(request):
    aircrafts = Aircraft.objects.all()
    return render(request, 'airlines/aircraft_list.html', {'aircrafts': aircrafts})





# -------------------------------------Create methods 
#@login_required
def airline_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        callsign = request.POST["callsign"]
        base_airport = request.POST["base_air"]
        founded_year = request.POST["founded_year"]

        new_airline = Airline(name=name,callsign=callsign,base_airport = base_airport,founded_year = founded_year)
        new_airline.save()
    return render(request,'airlines/airline_create.html')

#@login_required
def aircraft_create(request):
    airlines = Airline.objects.all()
    if request.method == "POST":
        serial_number = request.POST["serial_number"]
        type = request.POST["type"]
        model = request.POST["model"]
        engine = request.POST["engine"]
        op_airline = Airline.objects.get(id = request.POST["op_airline"])

        new_aircraft = Aircraft(manufacturer_serial_number = serial_number, type = type, model = model, number_of_engines = engine, operator_airline = op_airline)
        new_aircraft.save()


    return render(request,'airlines/aircraft_create.html',{"airlines":airlines})



 

# -------------------------------------Delete methods 
#@login_required
def airline_delete(request, id):
    airline = get_object_or_404(Airline, id = id)
    if request.method == "POST":
        airline.delete()
        return redirect("airline_list")

    return render(request, "airlines/airline_delete.html", {"airline":airline})

#@login_required
def aircraft_delete(request,id):
    aircraft = get_object_or_404(Aircraft,id = id)
    if request.method == "POST":
        aircraft.delete()
        return redirect("aircraft_list")
    return render(request,"airlines/aircraft_delete.html",{"aircraft":aircraft})





# -------------------------------------Update methods 
#@login_required
def airline_edit(request,id):
    airline = get_object_or_404(Airline, id = id)

    if request.method == "POST":
        name = request.POST["name"]
        callsign = request.POST["callsign"]
        base_airport = request.POST["base_air"]
        founded_year = request.POST["founded_year"]

        new_airline = Airline(id = id ,name=name,callsign=callsign,base_airport = base_airport,founded_year = founded_year)
        new_airline.save()
        return redirect("airline_list")

    return render(request, "airlines/airline_edit.html", {"airline":airline})

#@login_required
def aircraft_edit(request,id): 
    aircraft = get_object_or_404(Aircraft, id = id)
    airlines = Airline.objects.all()

    if request.method == "POST":
        serial_number = request.POST["serial_number"]
        type = request.POST["type"]
        model = request.POST["model"]
        engine = request.POST["engine"]
        op_airline = Airline.objects.get(id = request.POST["op_airline"])
        print(serial_number,type,model,engine, op_airline)

        updated_aircraft = Aircraft(id = id ,manufacturer_serial_number = serial_number, type = type, model = model, number_of_engines = engine, operator_airline = op_airline)

        updated_aircraft.save()
        return redirect("aircraft_list")


    return render(request, "airlines/aircraft_edit.html",
                {
                    "aircraft":aircraft,
                    "airlines":airlines,
                }
            )
