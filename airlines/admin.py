from django.contrib import admin
from airlines.models import Aircraft, Airline

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name","callsign","founded_year","base_airport")
    list_filter = ("callsign","founded_year","base_airport")
    search_fields = ("name","callsign","founded_year","base_airport")

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ("type","model","operator_airline",)
    list_filter = ("type","model","operator_airline")
    search_fields = ("type","model","operator_airline")


