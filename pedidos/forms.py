from django import forms
from .models import Pedido
from .choices import *

class PedidoForm(forms.ModelForm):
	conductor = forms.ChoiceField(choices=CONDUCTOR,label="Conductor",initial='',widget=forms.Select(),required=True)
	class Meta:
		model = Pedido
		fields = ['conductor','orden','operador','instalacion','cliente','destino','direccion','tfno','email','producto1','cantidad1','producto2','cantidad2','producto3','cantidad3']
		widgets = {
			'orden':forms.TextInput(attrs={'class':'form-control','placeholder':'Orden'}),
			'operador':forms.TextInput(attrs={'class':'form-control','placeholder':'Operador'}),
			'instalacion':forms.TextInput(attrs={'class':'form-control','placeholder':'Instalación'}),
			'cliente':forms.TextInput(attrs={'class':'form-control','placeholder':'Cliente'}),
			'destino':forms.TextInput(attrs={'class':'form-control','placeholder':'Destino'}),
			'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}),
			'tfno':forms.TextInput(attrs={'class':'form-control','placeholder':'Tfno'}),
			'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
			'producto1':forms.TextInput(attrs={'class':'form-control','placeholder':'Producto'}),
			'cantidad1':forms.TextInput(attrs={'class':'form-control','placeholder':'Cantidad'}),
			'producto2':forms.TextInput(attrs={'class':'form-control','placeholder':'Producto'}),
			'cantidad2':forms.TextInput(attrs={'class':'form-control','placeholder':'Cantidad'}),
			'producto3':forms.TextInput(attrs={'class':'form-control','placeholder':'Producto'}),
			'cantidad3':forms.TextInput(attrs={'class':'form-control','placeholder':'Cantidad'}),
			

		}
		labels = {
			'conductor':'Conductor',
			'orden':'',
			'operador':'',
			'instalacion':'',
			'cliente':'',
			'destino':'',
			'direccion':'',
			'tfno':'TFNO',
			'email':'',
			'producto1':'Producto',
			'cantidad1':'Cantidad',
			'producto2':'Producto',
			'cantidad2':'Cantidad',
			'producto3':'Producto',
			'cantidad3':'Cantidad',
		
		}
