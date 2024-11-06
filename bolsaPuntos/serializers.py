from rest_framework import serializers
from .models import BolsaPuntos
from datetime import date

class BolsaPuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BolsaPuntos
        fields = ['id', 'cliente', 'fecha_asignacion', 'fecha_caducidad', 'puntaje_asignado', 'puntaje_utilizado', 'saldo_puntos', 'monto_operacion']
        read_only_fields = ['fecha_asignacion', 'saldo_puntos']
    
    def validate_fecha_caducidad(self, value):
        # Validamos solo para evitar que la fecha de caducidad sea en el pasado
        if value <= date.today():
            raise serializers.ValidationError("La fecha de caducidad debe ser posterior a la fecha de hoy.")
        return value
