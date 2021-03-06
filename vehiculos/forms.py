from django import forms
from .models import Vehiculo, Compartimentos
from .choices import *

#prueba

class DateInput(forms.DateInput):
	input_type = 'date'

class VehiculoForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TIPO_VEHICULO,label="",initial='',widget=forms.Select(),required=True)
	class Meta:
		model = Vehiculo
		fields = ['tipo','matricula','ejes','tara','peso_maximo','carga_pesados','solo_gasoleos','no_petroliferos','carga_queroseno','equipo_adicional','equipos','contador','compart','fechaseguro','fechaadr','fechaitv','fechatablas','fechatarjetatte','observaciones']
		widgets = {
					'matricula':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
					'ejes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejes'}),
					'tara':forms.TextInput(attrs={'class':'form-control','placeholder':'Tara','type':'number'}),
					'peso_maximo':forms.TextInput(attrs={'class':'form-control','placeholder':'Peso Máximo','type':'number'}),
					'carga_pesados':forms.CheckboxInput(attrs={'class':'form-control'}),
					'solo_gasoleos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'no_petroliferos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'carga_queroseno':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipo_adicional':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipos':forms.Textarea(attrs={'class':'form-control','placeholder':'Indicar equipos adicionales'}),
					'contador':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contador'}),
					'compart':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compartimentos'}),
					'fechaseguro':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Seguro'}),
					'fechaadr':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha ADR'}),
					'fechaitv':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha ITV'}),
					'fechatablas':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tablas de Calibración'}),
					'fechatarjetatte':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tarjeta Tte'}),
					'observaciones':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
				}
		labels = {	'tipo':'',
					'matricula':'',
					'ejes':'',
					'tara':'',
					'peso_maximo':'',
					'equipos':'Indicar equipos adicionales',
					'contador':'',
					'compart':'',
					'fechaseguro':'Fecha Seguro',
					'fechaadr': 'Fecha ADR',
					'fechaitv':'Fecha ITV',
					'fechatablas':'Fecha Tablas de Calibración',
					'fechatarjetatte':'Fecha Tarjeta Tte',
					'observaciones':'Observaciones',
					}
"""
Mirar la forma de diferenciar formulario de tractora con semirremolque con cisterna
"""

class VehiculoUpdateForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TIPO_VEHICULO,label="",initial='',widget=forms.Select(),required=True)
	class Meta:
		model = Vehiculo
		fields = ['tipo','matricula','ejes','tara','peso_maximo','carga_pesados','solo_gasoleos','no_petroliferos','carga_queroseno','equipo_adicional','equipos','contador','compart','fechaseguro','fechaadr','fechaitv','fechatablas','fechatarjetatte','observaciones']
		widgets = {
					'matricula':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
					'ejes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejes'}),
					'tara':forms.TextInput(attrs={'class':'form-control','placeholder':'Tara','type':'number'}),
					'peso_maximo':forms.TextInput(attrs={'class':'form-control','placeholder':'Peso Máximo','type':'number'}),
					'carga_pesados':forms.CheckboxInput(attrs={'class':'form-control'}),
					'solo_gasoleos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'no_petroliferos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'carga_queroseno':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipo_adicional':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipos':forms.Textarea(attrs={'class':'form-control','placeholder':'Indicar equipos adicionales'}),
					'contador':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contador'}),
					'compart':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compartimentos'}),
					'fechaseguro':DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Fecha Seguro'}),
					'fechaadr':DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Fecha ADR'}),
					'fechaitv':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha ITV'}),
					'fechatablas':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tablas de Calibración'}),
					'fechatarjetatte':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tarjeta Tte'}),
					'observaciones':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
				}
		labels = {	'tipo':'',
					'matricula':'',
					'ejes':'',
					'tara':'',
					'peso_maximo':'',
					'equipos':'Indicar equipos adicionales',
					'contador':'Contador propio',
					'compart':'',
					'fechaseguro':'Fecha Seguro',
					'fechaadr': 'Fecha ADR',
					'fechaitv':'Fecha ITV',
					'fechatablas':'Fecha Tablas de Calibración',
					'fechatarjetatte':'Fecha Tarjeta Tte',
					'observaciones':'Observaciones',
					}

class VehiculoDetailForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TIPO_VEHICULO,label="",initial='',widget=forms.Select(),required=True)
	class Meta:
		model = Vehiculo
		fields = ['tipo','matricula','ejes','tara','peso_maximo','carga_pesados','solo_gasoleos','no_petroliferos','carga_queroseno','equipo_adicional','equipos','contador','compart','fechaadr','fechaitv','fechatablas','fechatarjetatte','observaciones']
		widgets = {
					'matricula':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
					'ejes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejes'}),
					'tara':forms.TextInput(attrs={'class':'form-control','placeholder':'Tara','type':'number'}),
					'peso_maximo':forms.TextInput(attrs={'class':'form-control','placeholder':'Peso Máximo','type':'number'}),
					'carga_pesados':forms.CheckboxInput(attrs={'class':'form-control'}),
					'solo_gasoleos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'no_petroliferos':forms.CheckboxInput(attrs={'class':'form-control'}),
					'carga_queroseno':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipo_adicional':forms.CheckboxInput(attrs={'class':'form-control'}),
					'equipos':forms.Textarea(attrs={'class':'form-control','placeholder':'Indicar equipos adicionales'}),
					'contador':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contador'}),
					'compart':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compartimentos'}),
					'fechaadr':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha ADR'}),
					'fechaitv':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha ITV'}),
					'fechatablas':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tablas de Calibración'}),
					'fechatarjetatte':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Fecha Tarjeta Tte'}),
					'observaciones':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
				}
		labels = {	'tipo':'',
					'matricula':'',
					'ejes':'',
					'tara':'',
					'peso_maximo':'',
					'equipos':'Indicar equipos adicionales',
					'contador':'',
					'compart':'',
					'fechaseguro':'fecha Seguro',
					'fechaadr': 'Fecha ADR',
					'fechaitv':'Fecha ITV',
					'fechatablas':'Fecha Tablas de Calibración',
					'fechatarjetatte':'Fecha Tarjeta Tte',
					'observaciones':'Observaciones',
					}

class SearchForm(forms.Form):
    query = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))


class CompartimentosForm(forms.ModelForm):
	class Meta:
		model = Compartimentos
		fields = ['compartimento','capacidad','altura','tag']
		widgets = {
			'compartimento': forms.TextInput(attrs={'class':'form-control','placeholder':'número de compartimento'}),
			'capacidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Capacidad'}),
			'altura': forms.TextInput(attrs={'class':'form-control','placeholder':'Altura en mm'}),
			'tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Código TAG'}),
		}
		labels = {
		'compartimento': '',
			'capacidad': '',
			'altura': '',
			'tag': '',
		}