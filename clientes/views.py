from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import ClienteSerializer
from .models import Cliente
from bolsaPuntos.models import BolsaPuntos
from django.utils import timezone
from rest_framework.response import Response 
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class=ClienteSerializer

    def create(self, request, *args, **kwargs):
        # Crear el nuevo cliente
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevo_cliente = serializer.save()

        # Verificar si el cliente fue referido por otro cliente
        referido_por_id = request.data.get('referido_por')
        puntos_bienvenida = 1  # Puntos para el nuevo cliente
        puntos_referido = 2   # Puntos para el cliente que refiere

        if referido_por_id:
            try:
                cliente_referente = Cliente.objects.get(id=referido_por_id)

                # Asignar puntos al cliente referente
                BolsaPuntos.objects.create(
                    cliente=cliente_referente,
                    fecha_caducidad=timezone.now() + timezone.timedelta(days=365),
                    puntaje_asignado=puntos_referido,
                    puntaje_utilizado=0,
                    saldo_puntos=puntos_referido,
                    monto_operacion=0,  # No hay operación de compra asociada
                    metodo_pago='Referido'
                )

            except Cliente.DoesNotExist:
                return Response({"error": "Cliente referente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Asignar puntos al nuevo cliente
        BolsaPuntos.objects.create(
            cliente=nuevo_cliente,
            fecha_caducidad=timezone.now() + timezone.timedelta(days=365),
            puntaje_asignado=puntos_bienvenida,
            puntaje_utilizado=0,
            saldo_puntos=puntos_bienvenida,
            monto_operacion=0,  # No hay operación de compra asociada
            metodo_pago='Bienvenida'
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

