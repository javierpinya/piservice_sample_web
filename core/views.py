from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
	template_name = "core/home.html"
	"""
	def get_context_data(self, **kwargs):
		# este método maneja el diccionario de contexto de la vista
		#con él podemos enviar todos los datos a la plantilla con
		# template_tags. ej: {{title}}
		context = super().get_context_data(**kwargs)
		context['title'] = "Mi super webplayground"
		return context
	"""
	def get(self, request): #este método maneja la respuesta de la vista. Podemos hacer lo mismo que en el get_context_data
		return render(request,self.template_name, {'title':"El Cargadero"})

class SamplePageView(TemplateView):
	template_name = "core/sample.html"