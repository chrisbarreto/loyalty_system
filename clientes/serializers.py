from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=["id","nombre","apellido","numero_documento","tipo_documento","nacionalidad","email","fecha_nacimiento","nivel"]

    def validate_referidor(self, value):
        # Validación para evitar que un cliente se refiera a sí mismo
        if self.instance and value == self.instance:
            raise serializers.ValidationError("Un cliente no puede referirse a sí mismo.")
        return value
