# consultas/serializers.py
from rest_framework import serializers
from .models import UsoPuntos

class UsoPuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoPuntos
        fields = ['cliente', 'concepto', 'puntaje_utilizado']