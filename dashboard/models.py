from django.db import models
from .models import UsoPuntos

class UsoPuntos(models.Model):
    puntaje_utilizado = models.IntegerField()
    monto_equivalente = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Uso de puntos: {self.puntaje_utilizado} - {self.monto_equivalente}"
