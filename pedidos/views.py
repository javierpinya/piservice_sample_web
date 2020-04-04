from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from .models import Pedido
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PedidoForm
from django.urls import reverse, reverse_lazy

# Create your views here.
class PedidoListView(ListView):
	model = Pedido

class PedidoCreateView(CreateView):
	model = Pedido
	form_class = PedidoForm
	template_name = "pedidos/pedido_form.html"
	success_url = reverse_lazy('pedidos:pedidos')