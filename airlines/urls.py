from django.urls import path
from . import views

urlpatterns = [
    path('airlines/', views.airline_list, name='airline-list'),
    path('aircrafts/', views.aircraft_list, name='aircraft-list'),
]
