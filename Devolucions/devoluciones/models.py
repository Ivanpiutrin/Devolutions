from django.db import models


class DevolucionCliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.PositiveIntegerField()
    cantidad = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    NombreVendedor = models.CharField(max_length=100)
    distribuidor = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    