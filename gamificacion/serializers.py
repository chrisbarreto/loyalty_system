from rest_framework import serializers
from .models import Insignia, Desafio, ProgresoUsuario

class InsigniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insignia
        fields = '__all__'

class DesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desafio
        fields = '__all__'

class ProgresoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoUsuario
        fields = '__all__'
