from django.db import models
from clientes.models import Cliente
from django.db import transaction  
from datetime import date 

#Clase para el criterio de edad de la segmentación
class Criterio(models.Model):
    descripcion = models.CharField(max_length=255)
    edad_minima = models.PositiveIntegerField(default=0)
    edad_maxima = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.descripcion} (Edad: {self.edad_minima}-{self.edad_maxima})"

    @classmethod
    def agregar(cls, descripcion, edad_minima, edad_maxima):
        return cls.objects.create(descripcion=descripcion, edad_minima=edad_minima, edad_maxima=edad_maxima)

    @classmethod
    def modificar(cls, id, nueva_descripcion, nueva_edad_minima, nueva_edad_maxima):
        criterio = cls.objects.get(id=id)
        criterio.descripcion = nueva_descripcion
        criterio.edad_minima = nueva_edad_minima
        criterio.edad_maxima = nueva_edad_maxima
        criterio.save()
        return criterio

    @classmethod
    def eliminar(cls, id):
        criterio = cls.objects.get(id=id)
        criterio.delete()


#Clase para guardar los datos de los clientes y las segmentaciones en las que aparece
class Segmentacion(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #Método para calcular y segmentar por edad
    @classmethod
    def segmentar_por_edad(cls):
        fecha_hoy = date.today()
        clientes = Cliente.objects.all()

        with transaction.atomic():
            cls.objects.all().delete()  

            for cliente in clientes:
                #Se calcula la edad del cliente
                edad = (fecha_hoy - cliente.fecha_nacimiento).days // 365


                for criterio in Criterio.objects.all():
                    if criterio.edad_minima <= edad <= criterio.edad_maxima:
                        cls.objects.create(criterio=criterio, cliente=cliente)

    def __str__(self):
        return f"Cliente {self.cliente.nombre} Segmento: {self.criterio.descripcion}"

    @classmethod
    def agregar(cls, id_criterio, cliente_id):
        criterio = Criterio.objects.get(id=id_criterio)
        return cls.objects.create(criterio=criterio, cliente_id=cliente_id)

    @classmethod
    def modificar(cls, id, nuevo_id_criterio, nuevo_cliente_id):
        segmentacion = cls.objects.get(id=id)
        segmentacion.criterio = Criterio.objects.get(id=nuevo_id_criterio)
        segmentacion.cliente_id = nuevo_cliente_id
        segmentacion.save()
        return segmentacion

    @classmethod
    def eliminar(cls, id):
        segmentacion = cls.objects.get(id=id)
        segmentacion.delete()


#Clase para los beneficios asociados a las segmentaciones basados en los criterios
class Beneficio(models.Model):
    descripcion = models.CharField(max_length=255)
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    @classmethod
    def agregar(cls, descripcion, id_criterio):
        criterio = Criterio.objects.get(id=id_criterio)
        return cls.objects.create(descripcion=descripcion, criterio=criterio)

    @classmethod
    def modificar(cls, id, nueva_descripcion, nuevo_id_criterio):
        beneficio = cls.objects.get(id=id)
        beneficio.descripcion = nueva_descripcion
        beneficio.criterio = Criterio.objects.get(id=nuevo_id_criterio)
        beneficio.save()
        return beneficio

    @classmethod
    def eliminar(cls, id):
        beneficio = cls.objects.get(id=id)
        beneficio.delete()