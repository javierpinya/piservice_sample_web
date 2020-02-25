from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Vehiculo
from .forms import VehiculoForm,VehiculoUpdateForm
# Create your views here.

class StaffRequiredMixin(object):
	"""
	Este mixin requerirá que el usuario sea miembro del staff
	"""
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(VehiculoCreateView,self).dispatch(request,*args,**kwargs)

class VehiculoListView(ListView):
	model = Vehiculo

class VehiculoDetailView(DetailView):
	model = Vehiculo

@method_decorator(staff_member_required,name='dispatch')
class VehiculoCreateView(CreateView):
	model = Vehiculo
	form_class = VehiculoForm
	template_name="vehiculos/vehiculo_form.html"
	success_url = reverse_lazy('vehiculos:vehiculos')

	
@method_decorator(staff_member_required,name='dispatch')
class VehiculoUpdateView(UpdateView):
	model = Vehiculo
	form_class = VehiculoUpdateForm
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse_lazy('vehiculos:update_vehiculo', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required,name='dispatch')
class VehiculoDeleteView(DeleteView):
	model = Vehiculo
	success_url = reverse_lazy('vehiculos:vehiculos')