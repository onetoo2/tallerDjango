from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.clientes.models import Cliente
from apps.clientes.forms import ClienteForm
# Create your views here.
def index(request):
	#return HttpResponse("Esta es la respuesta")
	return render(request, 'clientes/index.html')

def plantilla(request):
	return render(request, 'clientes/index.html')

def especial(request):
	return render(request, 'clientes/paginaEspecial.html')

def especial2(request):
	contexto = {
	'clientes':Cliente.objects.all()
	}
	return render(request, 'clientes/paginaEspecial.html', contexto)

'''def especial2(request):
	return render(request, 'clientes/paginaEspecial.html', {clientes:Cliente.objects.all()})'''

class ViewCliente(ListView):
	model = Cliente
	#queryset si es necesario
	#queryset = Cliente.objects.filter(nombre='Juan')
	template_name = 'clientes/infoClientes.html'

#-----------------------------------

def nuevoRegistro(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('clientes:listaClientes')
	else:
		form = ClienteForm()
	return render(request, 'clientes/nuevoFormulario.html', {'form': form})


def editarRegistro(request, idCliente):
	cliente = Cliente.objects.get(id = idCliente)
	if(request.method == 'GET'):
		form = ClienteForm(instance=cliente)
	else:
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save();
		return redirect('clientes:listaClientes')
	return render(request, 'clientes/nuevoFormulario.html', {'form': form})


def eliminarRegistro(request, idCliente):
	cliente = Cliente.objects.get(id = idCliente)
	if(request.method == 'GET'):
		cliente.delete()
		return redirect('clientes:listaClientes')


















