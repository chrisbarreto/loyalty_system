from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    numero_documento=models.CharField(max_length=50,unique =True)
    tipo_documento=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return f"{self.nombre}{self.apellido}"
    