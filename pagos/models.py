from django.db import models

# Create your models here.
class Pago(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=50)  # Por ejemplo, 'PayPal', 'Tarjeta de Crédito', etc.
    estado = models.CharField(max_length=20, default='pendiente')  # 'aprobado', 'rechazado'

    def __str__(self):
        return f"Pago de {self.monto} Gs. por {self.cliente.nombre}"
