from django.db import models
#from ckeditor.fields import RichTextField
from .choices import *



# Create your models here.
class Vehiculo(models.Model):
	tipo = models.IntegerField(choices=TIPO_VEHICULO,default=1,verbose_name='Tipo de Vehículo')
	matricula = models.CharField(verbose_name='Matrícula',max_length=8)
	avatar = models.ImageField(upload_to='profiles',null=True, blank=True)
	ejes = models.IntegerField(verbose_name='Ejes',blank=True,null=True)
	tara = models.IntegerField(verbose_name='Tara',blank=True,null=True)
	peso_maximo = models.IntegerField(verbose_name='Peso Máximo',blank=True,null=True)
	carga_pesados = models.BooleanField(verbose_name='Carga Pesados',default=False)
	solo_gasoleos = models.BooleanField(verbose_name='Sólo Gasóleos',default=False)
	no_petroliferos = models.BooleanField(verbose_name='No Petrolíferos',default=False)
	carga_queroseno = models.BooleanField(verbose_name='Carga Queroseno',default=False)
	equipo_adicional = models.BooleanField(verbose_name='Equipo Adicional', default=False)
	#equipos = RichTextField(verbose_name='Indicar equipos adicionales',null=True,blank=True)
	equipos = models.CharField(verbose_name='Indicar equipos adicionales',null=True,blank=True,max_length=500)
	contador = models.BooleanField(verbose_name='Contador', blank=True,null=True)
	compartimentos = models.IntegerField(verbose_name='Compartimentos',blank=True,null=True)
	tipo_adr = models.CharField(verbose_name='Tipo ADR',max_length=8,blank=True,null=True)
	fechaadr = models.DateField(verbose_name='Fecha ADR')
	fechaitv = models.DateField(verbose_name='Fecha ITV')
	fechatablas = models.DateField(verbose_name='Fecha Tablas Calibración')
	fechatarjetatte = models.DateField(verbose_name='Fecha Tarjeta Tte')
	#observaciones = RichTextField(verbose_name='Observaciones',null=True,blank=True)
	observaciones = models.CharField(verbose_name='Observaciones',null=True,blank=True,max_length=500)
	editado = models.DateTimeField(auto_now=True,verbose_name='Editado')
	creado = models.DateTimeField(auto_now_add=True,verbose_name='Creado')

	class Meta:
		verbose_name = "vehículo"
		verbose_name_plural = "vehículos"
		ordering = ['matricula','editado']

	def __str__(self):
		return self.matricula

