from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length = 30)
	apellidos = models.CharField(max_length = 30)

class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente, null= True, blank = True, on_delete = models.CASCADE)
	