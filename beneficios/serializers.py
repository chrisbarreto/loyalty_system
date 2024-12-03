from rest_framework import serializers
from .models import Beneficios 

class BeneficiosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Beneficios
        fields="__all__"
        