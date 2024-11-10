from django.db import models
from clientes.models import Cliente
from bolsaPuntos.models import BolsaPuntos

class UsoPuntosCabecera(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='usos_puntos')
    puntaje_utilizado = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    concepto_uso = models.CharField(max_length=255)  # Ejemplo: "Descuento", "Vale de consumo"

    def __str__(self):
        return f"Uso de puntos del cliente {self.cliente.id} - {self.puntaje_utilizado} puntos"

class UsoPuntosDetalle(models.Model):
    cabecera = models.ForeignKey(UsoPuntosCabecera, on_delete=models.CASCADE, related_name='detalles')
    bolsa_puntos = models.ForeignKey(BolsaPuntos, on_delete=models.CASCADE, related_name='usos')
    puntaje_utilizado = models.PositiveIntegerField()

    def __str__(self):
        return f"Detalle uso puntos - Cabecera {self.cabecera.id} - {self.puntaje_utilizado} puntos"
