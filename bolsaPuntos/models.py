
from django.db import models
from clientes.models import Cliente  # Importar el modelo Cliente para la relación

# Create your models here.
class BolsaPuntos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='bolsas_puntos')
    fecha_asignacion=models.DateTimeField(auto_now_add=True)
    fecha_caducidad=models.DateField()
    puntaje_asignado=models.PositiveIntegerField()
    puntaje_utilizado=models.PositiveIntegerField(default=0)
    saldo_puntos=models.PositiveIntegerField(editable=False)
    monto_operacion=models.DecimalField(max_digits=10,decimal_places=2)

    def save(self, *args,**kwargs):
        #Actualizar saldo de puntos antes de guardar
        self.saldo_puntos=self.puntaje_asignado -self.puntaje_utilizado
        super().save(*args,**kwargs)

    def __str__(self):
        return f'Bolsa de puntos de{self.cliente.nombre} ({self.puntaje_asignado} puntos)'