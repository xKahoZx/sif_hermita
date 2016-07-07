from sif.apps.inventario.models import *
from django import forms


class busqueda_form(forms.Form):
<<<<<<< HEAD

	
	fecha_inicio 	=	forms.CharField(widget = forms.DateInput())
	fecha_fin 		=	forms.CharField(widget = forms.DateInput())

	
=======
	fecha_inicio = forms.CharField(widget = forms.DateInput())
	fecha_fin = forms.CharField(widget = forms.TextInput())
	
	
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
