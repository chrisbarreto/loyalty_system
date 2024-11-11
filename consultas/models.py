from django.db import models
from clientes.models import Cliente 
from conceptos.models import Concepto

class UsoPuntos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    puntaje_utilizado = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nombre} uso {self.puntaje_utilizado} puntos en concepto de {self.concepto.descripcion}"
