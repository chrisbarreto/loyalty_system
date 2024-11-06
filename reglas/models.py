from django.db import models

# Create your models here.
class Reglas(models.Model):
    limite_inferior=models.IntegerField()
    limite_superior=models.IntegerField()
    monto=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.limite_inferior} a {self.limite_superior} : {self.monto}"
 