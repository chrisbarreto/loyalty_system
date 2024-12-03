from django.db import models
from django.core.exceptions import ValidationError
from niveles.models import Niveles
from datetime import date
# Create your models here.
class Promocion(models.Model):
    TIPO_PROMOCION=[
        ('descuento','Descuento'),
        ('bonificacion','Bonificacion')
    ]

    descripcion=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    duracion_dias=models.IntegerField(editable=False)
    nivel=models.ForeignKey(Niveles, on_delete=models.CASCADE, related_name='nivel', blank=True, null=True)
    tipo=models.CharField(max_length=30, choices=TIPO_PROMOCION)
    descuento=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    producto=models.CharField(max_length=100, null=True, blank=True)
    bonificacion=models.PositiveIntegerField(null=True,blank=True)

    #Comprueba si la vigencia de la promo
    @property
    def activo(self):
        fecha_hoy=date.today()
        if self.fecha_fin<fecha_hoy:
            return False
        return True


    TIPOS_VALIDOS=['descuento', 'bonificacion']

    def clean(self):
        print('ejecutando')
        if self.tipo not in self.TIPOS_VALIDOS:
            raise ValidationError(f"El tipo de promocion no es valido. Opciones: {self.TIPOS_VALIDOS}")
        if self.tipo == 'descuento':
            if not self.descuento:
                raise ValidationError('El valor es obligatorio para promociones de tipo descuento.')
            if self.bonificacion:
                raise ValidationError("Estas asignando una bonificacion a una promocion de tipo 'descuento'")
        if self.tipo == 'bonificacion':
            if not self.bonificacion:
                raise ValidationError('La bonificacion es obligatoria para promociones de tipo bonificación de puntos.')
            if self.producto:
                raise ValidationError('Las bonificaciones de puntos son globales. No se relacionan con un producto especifico')
            if self.descuento:
                raise ValidationError("Estas asignando un descuento a una promocion de tipo 'bonificacion'")
        if self.fecha_inicio>self.fecha_fin:
            raise ValidationError('La fecha fin no puede ser menor a la fecha inicio.')


    def save(self,*args,**kwargs):
        self.full_clean()
        diferencia = self.fecha_fin - self.fecha_inicio
        self.duracion_dias=diferencia.days

        return super(Promocion,self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.fecha_inicio} a {self.fecha_fin} : {self.duracion_dias}"
