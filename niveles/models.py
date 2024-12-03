from django.db import models

class Niveles(models.Model):
    puntaje_min=models.IntegerField(unique=True)
    puntaje_max=models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.puntaje_min} a {self.puntaje_max}"