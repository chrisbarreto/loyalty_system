from django.db import models
from django.db.models.functions import ExtractDay
from django.db.models.fields import DurationField
# Create your models here.
class Vencimiento(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    duracion_dias=models.IntegerField(editable=False) 

    def save(self,*args,**kwargs):
        delta = self.fecha_fin - self.fecha_inicio
        self.duracion_dias=delta.days

        return super(Vencimiento,self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.fecha_inicio} a {self.fecha_fin} : {self.duracion_dias}"
 