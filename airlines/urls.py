from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.airline_list, name="index"),
    path("airline/create-airline/",views.airline_create, name="airline_create"),
    path('airline/', views.airline_list, name="airline_list"),
    path("airline/edit-airline/<int:id>",views.airline_edit, name = "airline_edit"),
    path("airline/delete-airline/<int:id>",views.airline_delete, name = "airline_delete"),

    path("aircraft/create-aircraft/",views.aircraft_create, name="aircraft_create"),
    path('aircraft/', views.aircraft_list, name="aircraft_list"),
    path("aircraft/edit-aircraft/<int:id>",views.aircraft_edit, name = "aircraft_edit"),
    path("aircraft/delete-aircraft/<int:id>",views.aircraft_delete, name = "aircraft_delete"),


    path('api/airline/', views.AirlineListCreateView.as_view(), name='airline-list-create'),
    path('api/airline/<int:pk>/', views.AirlineDetailView.as_view(), name='airline-detail'),

    path('api/aircraft/', views.AircraftListCreateView.as_view(), name='aircraft-list-create'),
    path('api/aircraft/<int:pk>/', views.AircraftDetailView.as_view(), name='aircraft-detail'),
]
