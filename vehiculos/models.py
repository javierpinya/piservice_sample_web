from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Vehiculo(models.Model):
	tipo = models.CharField(verbose_name='Tipo de Vehículo',max_length=1)
	matricula = models.CharField(verbose_name='Matrícula',max_length=8)
	avatar = models.ImageField(upload_to='profiles',null=True, blank=True)
	ejes = models.IntegerField(verbose_name='Ejes',blank=True,null=True)
	contador = models.BooleanField(verbose_name='Contador', blank=True,null=True)
	compartimentos = models.IntegerField(verbose_name='Compartimentos',blank=True,null=True)
	fechaadr = models.DateTimeField(verbose_name='Fecha ADR')
	fechaitv = models.DateTimeField(verbose_name='Fecha ITV')
	fechatablas = models.DateTimeField(verbose_name='Fecha Tablas Calibración')
	fechaarnes = models.DateTimeField(verbose_name='Fecha Arnés')
	fechatablas = models.DateTimeField(verbose_name='Fecha Tablas Calibración')
	observaciones = RichTextField(verbose_name='Observaciones',null=True,blank=True)
	editado = models.DateTimeField(auto_now=True,verbose_name='Editado')
	creado = models.DateTimeField(auto_now_add=True,verbose_name='Creado')

	class Meta:
		verbose_name = "vehículo"
		verbose_name_plural = "vehículos"
		ordering = ['matricula','editado']

	def __str__(self):
		return self.matricula

