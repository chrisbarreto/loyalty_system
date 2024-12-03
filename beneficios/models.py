from django.db import models
from niveles.models import Niveles
# Create your models here.
class Beneficios(models.Model):
    nivel=models.ForeignKey(Niveles,on_delete=models.CASCADE, related_name='niveles',default=1)
    descuento=models.FloatField(default=0.0)


    