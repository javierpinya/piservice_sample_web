from django.urls import path
from .views import VehiculoListView,VehiculoDetailView,VehiculoCreateView,VehiculoUpdateView,VehiculoDeleteView

vehiculos_patterns = ([
    path('', VehiculoListView.as_view(), name="vehiculos"),
    path('<int:pk>/<slug:slug>', VehiculoDetailView.as_view(), name="vehiculo"),
    path('update/<int:pk>', VehiculoUpdateView.as_view(), name="update_vehiculo"),
    path('create/', VehiculoCreateView.as_view(), name="create_vehiculo"),
    path('delete/<int:pk>', VehiculoDeleteView.as_view(), name="delete_vehiculo"),
], 'vehiculos')