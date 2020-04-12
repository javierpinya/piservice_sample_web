from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from .choices import *



# Create your models here.
class Vehiculo(models.Model):
	tipo = models.IntegerField(choices=TIPO_VEHICULO,default=1,verbose_name='Tipo de Vehículo')
	nacion = models.IntegerField(choices=NACION,default=2,verbose_name='Nación')
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
	contador = models.CharField(verbose_name='Contador',null=True,blank=True,max_length=1)
	equipos = models.CharField(verbose_name='Indicar equipos adicionales',null=True,blank=True,max_length=500)
	compart = models.IntegerField(verbose_name='Compartimentos',blank=True,null=True)
	fechaseguro = models.DateField(verbose_name='Fecha vencimiento seguro')
	tipo_adr = models.CharField(verbose_name='Tipo ADR',max_length=8,blank=True,null=True)
	fechaadr = models.DateField(verbose_name='Fecha ADR')
	fechaitv = models.DateField(verbose_name='Fecha ITV')
	fechatablas = models.DateField(verbose_name='Fecha Tablas Calibración')
	fechatarjetatte = models.DateField(verbose_name='Fecha Tarjeta Tte')
	#observaciones = RichTextField(verbose_name='Observaciones',null=True,blank=True)
	observaciones = models.CharField(verbose_name='Observaciones',null=True,blank=True,max_length=500)
	editado = models.DateTimeField(auto_now=True,verbose_name='Editado')
	creado = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
	creado_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "vehículo"
		verbose_name_plural = "vehículos"
		ordering = ['matricula','editado']

	def __str__(self):
		return self.matricula

class Compartimentos(models.Model):
	camion = models.ForeignKey(Vehiculo,on_delete=models.CASCADE,default=0)
	compartimento = models.IntegerField(verbose_name='Comparimento',blank=True,null=True)
	capacidad = models.IntegerField(verbose_name='Capacidad', blank=True,null=True)
	altura = models.IntegerField(verbose_name='Altura',blank=True,null=True)
	tag = models.CharField(verbose_name='TAG',max_length=10,blank=True,null=True)

	class Meta:
		verbose_name='compartimento'
		verbose_name_plural = 'compartimentos'
		ordering = ['compartimento']

	def __str__(self):
		return self.tag
