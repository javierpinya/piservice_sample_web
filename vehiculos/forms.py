from django import forms
from .models import Vehiculo

class DateInput(forms.DateInput):
	input_type = 'date'

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = ['tipo','matricula','ejes','contador','compartimentos','fechaadr','fechaitv','fechatablas','fechaarnes','observaciones']
		widgets = {	'tipo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo Vehículo'}),
					'matricula':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
					'ejes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejes'}),
					'contador':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contador'}),
					'compartimentos':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compartimentos'}),
					'fechaadr':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha ADR'}),
					'fechaitv':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha ITV'}),
					'fechatablas':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha Tablas de Calibración'}),
					'fechaarnes':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha Arnés'}),
					'observaciones':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
				}
		labels = {	'tipo':'',
					'matricula':'',
					'ejes':'',
					'contador':'',
					'compartimentos':'',
					'fechaadr': 'Fecha ADR',
					'fechaitv':'Fecha ITV',
					'fechatablas':'Fecha Tablas de Calibración',
					'fechaarnes':'Fecha Arnés',
					'observaciones':'',
					}

class VehiculoUpdateForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = ['tipo','matricula','ejes','contador','compartimentos','fechaadr','fechaitv','fechatablas','fechaarnes','observaciones']
		widgets = {	'tipo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo Vehículo'}),
					'matricula':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
					'ejes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejes'}),
					'contador':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contador'}),
					'compartimentos':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compartimentos'}),
					'fechaadr':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha ADR'}),
					'fechaitv':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha ITV'}),
					'fechatablas':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha Tablas de Calibración'}),
					'fechaarnes':DateInput(attrs={'class':'form-control', 'placeholder':'Fecha Arnés'}),
					'observaciones':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
					}
		labels = {	'tipo':'',
					'matricula':'',
					'ejes':'',
					'contador':'',
					'compartimentos':'',
					'fechaadr': 'Fecha ADR',
					'fechaitv':'Fecha ITV',
					'fechatablas':'Fecha Tablas de Calibración',
					'fechaarnes':'Fecha Arnés',
					'observaciones':'',
					}