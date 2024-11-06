from rest_framework import serializers
from .models import Vencimiento

class VencimientoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model= Vencimiento
        read_only_fields=("duracion_dias",)
        fields="__all__"
 