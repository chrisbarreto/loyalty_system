from rest_framework import serializers
from .models import Reglas

class ReglasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reglas
        fields="__all__"
 