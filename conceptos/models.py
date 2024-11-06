from django.db import models

# Create your models here.

# Create your models here.
class Concepto(models.Model):
    descripcion=models.CharField(max_length=100)
    puntos_requeridos=models.IntegerField()

    def __str__(self):
        return f"{self.descripcion}"
    