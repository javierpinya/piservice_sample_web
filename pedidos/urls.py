from django.urls import path
from . import views
from .views import PedidoListView, PedidoCreateView

pedidos_patterns = ([
    path('', PedidoListView.as_view(), name="pedidos"),
    path('nuevo_pedido/',PedidoCreateView.as_view(),name="nuevo"),
], 'pedidos')