from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Vehiculo
from .forms import VehiculoForm,VehiculoUpdateForm,VehiculoDetailForm,SearchForm,CompartimentosForm
from django.db.models import Q
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
	template_name = "vehiculos/vehiculo_detail.html"
	form_class = VehiculoDetailForm

	def get_success_url(self):
		return reverse_lazy('vehiculos:update_vehiculo', args=[self.object.id])

@method_decorator(staff_member_required,name='dispatch')
class VehiculoCreateView(CreateView):
	model = Vehiculo
	form_class = VehiculoForm
	template_name="vehiculos/vehiculo_form.html"
	success_url = reverse_lazy('vehiculos:vehiculos')

	#def get_success_url(self):
		#return reverse_lazy('vehiculos:create_compartimento', args=[self.object.id])

@method_decorator(staff_member_required,name='dispatch')
class CompartimentoCreateView(CreateView):
	form_class = CompartimentosForm
	template_name = "vehiculos/vehiculo_compartimentos.html"
	success_url = reverse_lazy('vehiculos:vehiculos')

	def get_object(self):
		return Compartimentos.objects.get_or_create(camion=self.request.GET)

	def get_success_url(self):
		return reverse_lazy('vehiculos:create_compartimento',args=[self.object.id]) + '?ok'


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

@method_decorator(staff_member_required,name='dispatch')
class VehiculoSearchView(ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculo_search.html"

    def get_context_data(self,request,*args,**kwargs):
        queryset = request.GET.get("buscar")
        if(queryset):
            vehiculos = Vehiculo.objects.filter(
                Q(matricula = queryset) |
                Q(observaciones = queryset)
            ).distinct()
        return reverse_lazy('vehiculos:vehiculos',args=[self.object.id])

def vehiculo_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Vehiculo.objects.filter(matricula__icontains=query) | Vehiculo.objects.filter(tipo__icontains=query)
    return render(request,
                'vehiculos/vehiculo_search.html',
                {'form':form,'query':query,'results':results})

def vehiculo_prueba(request,pk):
	return HttpResponse("Estás buscando el siguiente coche %s." % pk)

def index(request):
	ultimos_coches = Vehiculo.objects.order_by('-matricula')[:4]
	context = {
		'ultimos_coches':ultimos_coches,
	}
	return render(request, 'vehiculos/index.html',context)

def detail(request,pk):
	try:
		coche = Vehiculo.objects.get(pk=pk)
	except Vehiculo.DoesNotExist:
		raise Http404("Coche no existe")
	return render(request,"vehiculos/detail.html",{'coche':coche})
		