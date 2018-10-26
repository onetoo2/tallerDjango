from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = {
			'nombre',
			'apellidos',
		}

		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
		}