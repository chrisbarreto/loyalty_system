from rest_framework import serializers

class PagoSerializer(serializers.Serializer):
    cliente_id = serializers.IntegerField()
    monto = serializers.DecimalField(max_digits=10, decimal_places=2)
