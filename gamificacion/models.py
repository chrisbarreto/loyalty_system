from django.db import models
from django.contrib.auth.models import User

class Insignia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='insignias/')
    puntos_requeridos = models.IntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Desafio(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    meta_puntos = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.titulo

    def esta_activo(self):
        from django.utils.timezone import now
        return self.fecha_inicio <= now() <= self.fecha_fin

class ProgresoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE)
    puntos_acumulados = models.IntegerField(default=0)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuario} - {self.desafio}'
