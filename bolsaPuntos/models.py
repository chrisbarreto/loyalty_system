
from django.db import models
from clientes.models import Cliente  # Importar el modelo Cliente para la relación

# Create your models here.
class BolsaPuntos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='bolsas_puntos')
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_caducidad = models.DateField()
    puntaje_asignado = models.PositiveIntegerField()
    puntaje_utilizado = models.PositiveIntegerField(default=0)
    saldo_puntos = models.PositiveIntegerField(default=0)

    monto_operacion = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Asegurarse de que el saldo de puntos no sea negativo y esté actualizado antes de guardar
        if not self.pk:  # Solo establece el saldo inicialmente cuando se crea la bolsa
            self.saldo_puntos = self.puntaje_asignado
        else:
            # Asegurarse de que el saldo de puntos se actualiza correctamente durante cualquier operación de uso
            self.saldo_puntos = max(0, self.puntaje_asignado - self.puntaje_utilizado)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Bolsa de puntos de {self.cliente.nombre} ({self.puntaje_asignado} puntos)'
