from django.db import models
from .choices import *

# Create your models here.
class Conductor(models.Model):
	dni = models.CharField(verbose_name='DNI',max_length=9)
	nombre = models.CharField(verbose_name='Nombre',max_length=20)
	apellidos = models.CharField(verbose_name='Apellidos',max_length=30)
	movil = models.CharField(verbose_name='Móvil',max_length=13)
	email = models.EmailField(verbose_name='Email',max_length=30)
	


class Pedido(models.Model):
	orden = models.CharField(verbose_name='Número de orden',max_length=12)
	operador = models.CharField(verbose_name='Operador',max_length=20,blank=True,null=True)
	instalacion = models.CharField(verbose_name='Instalación',max_length=20,blank=True,null=True)
	cliente = models.CharField(verbose_name='Cliente',max_length=50,blank=True,null=True)
	destino = models.CharField(verbose_name='Destino',max_length=50,blank=True,null=True)
	direccion = models.CharField(verbose_name='Dirección',max_length=80,blank=True,null=True)
	tfno = models.IntegerField(verbose_name='Teléfono',default=0,blank=True,null=True)
	email = models.EmailField(verbose_name='Email',max_length=30)
	driver = models.IntegerField(choices=CONDUCTOR,default=1,verbose_name='Conductor')
	producto1 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad1 = models.IntegerField(verbose_name='Cantidad',default=0)
	producto2 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad2 = models.IntegerField(verbose_name='Cantidad',default=0)
	producto3 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad3 = models.IntegerField(verbose_name='Cantidad',default=0)
	producto4 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad4 = models.IntegerField(verbose_name='Cantidad',default=0)
	producto5 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad5 = models.IntegerField(verbose_name='Cantidad',default=0)
	producto6 = models.CharField(verbose_name='Producto',max_length=10,blank=True,null=True)
	cantidad6 = models.IntegerField(verbose_name='Cantidad',default=0)
 




