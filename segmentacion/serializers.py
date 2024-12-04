from rest_framework import serializers
from .models import Segmentacion, Criterio, Beneficio

class SegmentacionSerializer(serializers.ModelSerializer):
    criterio_descripcion = serializers.CharField(source='criterio.descripcion', read_only=True)

    class Meta:
        model = Segmentacion
        fields = ['id', 'cliente', 'criterio', 'criterio_descripcion']

class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio
        fields = '__all__'


class BeneficioSerializer(serializers.ModelSerializer):
    criterio = serializers.PrimaryKeyRelatedField(queryset=Criterio.objects.all())  

    class Meta:
        model = Beneficio
        fields = ['id', 'descripcion', 'criterio'] 