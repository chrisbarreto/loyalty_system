from rest_framework import serializers
from .models import UsoPuntosCabecera, UsoPuntosDetalle

class UsoPuntosDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoPuntosDetalle
        fields = ['id', 'cabecera', 'bolsa_puntos', 'puntaje_utilizado']

class UsoPuntosCabeceraSerializer(serializers.ModelSerializer):
    detalles = UsoPuntosDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = UsoPuntosCabecera
        fields = ['id', 'cliente', 'puntaje_utilizado', 'fecha', 'concepto_uso', 'detalles']
