from django.contrib import admin
from .models import Vehiculo, Compartimentos
	
# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('matricula','tipo')

	# Inyectamos nuestro fichero css
	class Media:
		css = {
			'all':('vehiculos/css/custom_ckeditor.css',)
		}

class CompartimentosAdmin(admin.ModelAdmin):
	#list_display = ('tag')

	# Inyectamos nuestro fichero css
	class Media:
		css = {
			'all':('vehiculos/css/custom_ckeditor.css',)
		}

admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Compartimentos,CompartimentosAdmin)