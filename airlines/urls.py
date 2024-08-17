from django.urls import path
from .views import AirlineListCreateView, AirlineDetailView, AircraftListCreateView, AircraftDetailView

urlpatterns = [
    path('airline/', AirlineListCreateView.as_view(), name='airline-list-create'),
    path('airline/<int:pk>/', AirlineDetailView.as_view(), name='airline-detail'),
    path('aircraft/', AircraftListCreateView.as_view(), name='aircraft-list-create'),
    path('aircraft/<int:pk>/', AircraftDetailView.as_view(), name='aircraft-detail'),
]
