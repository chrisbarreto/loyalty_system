from rest_framework import serializers
from .models import Niveles

class NivelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveles
        fields = "__all__"