from django.urls import path
from apps.clientes.views import index, plantilla, especial, especial2, ViewCliente, nuevoRegistro, editarRegistro, eliminarRegistro

app_name = 'clientes'

urlpatterns = [
	path('', index),
	path('index/', index),
	path('plantilla', plantilla, name = "plantilla"),
	path('especial', especial),
	path('especial2', especial2),
	path('especial3', ViewCliente.as_view(), name = "listaClientes"),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarRegistro/<idCliente>', editarRegistro, name="editarRegistro"),
	path('eliminarRegistro/<idCliente>', eliminarRegistro, name="eliminarRegistro"),
]
