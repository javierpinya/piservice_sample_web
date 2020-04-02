from django.urls import path
from . import views
from .views import VehiculoListView,VehiculoDetailView,VehiculoCreateView,CompartimentoCreateView,VehiculoUpdateView,VehiculoDeleteView,VehiculoSearchView

vehiculos_patterns = ([
    path('', VehiculoListView.as_view(), name="vehiculos"),
    path('<int:pk>/<slug:slug>', VehiculoDetailView.as_view(), name="vehiculo"),
    path('update/<int:pk>', VehiculoUpdateView.as_view(), name="update_vehiculo"),
    path('create/', VehiculoCreateView.as_view(), name="create_vehiculo"),
    path('compartimentos/<int:pk>', CompartimentoCreateView.as_view(), name="create_compartimento"),
    path('delete/<int:pk>', VehiculoDeleteView.as_view(), name="delete_vehiculo"),
    path('buscar/', views.vehiculo_search, name="vehiculo_search"),
   	path('prueba/<int:pk>/',views.vehiculo_prueba,name="vehiculo_prueba"),
   	path('index/',views.index,name="index"),
   	path('detail/<int:pk>',views.detail,name="detail"),
], 'vehiculos')