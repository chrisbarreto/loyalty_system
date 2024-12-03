from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=["id","nombre","apellido","numero_documento","tipo_documento","nacionalidad","email","fecha_nacimiento","nivel"]
        