from rest_framework import serializers
from .models import Concepto

class ConceptoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Concepto
        fields="__all__"
 