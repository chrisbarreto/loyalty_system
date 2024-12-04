from django.db import models
from django.apps import apps
from niveles.models import Niveles
# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    numero_documento=models.CharField(max_length=50,unique =True)
    tipo_documento=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    referidor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referidos')

    @property
    def nivel(self):
        BolsaPuntos=apps.get_model('bolsaPuntos','BolsaPuntos')
        bolsas=BolsaPuntos.objects.filter(cliente=self)
        niveles=Niveles.objects.all().order_by('puntaje_min')
        puntos=0
        nivel_actual=1

        for bolsa in bolsas:
            puntos+=bolsa.saldo_puntos

        for nivel in niveles:
            if puntos>nivel.puntaje_min and puntos<nivel.puntaje_max:
                nivel_actual=nivel.pk
                break

        return nivel_actual

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    