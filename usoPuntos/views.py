from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import UsoPuntosCabecera, UsoPuntosDetalle
from .serializers import UsoPuntosCabeceraSerializer
from bolsaPuntos.models import BolsaPuntos

class UsoPuntosCabeceraViewSet(viewsets.ModelViewSet):
    queryset = UsoPuntosCabecera.objects.all()
    serializer_class = UsoPuntosCabeceraSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():  # Usar transacción para asegurar consistencia
            cliente_id = request.data.get('cliente')
            puntaje_requerido = request.data.get('puntaje_utilizado')
            concepto_uso = request.data.get('concepto_uso')

            # Obtener las bolsas de puntos del cliente ordenadas por fecha de asignación (FIFO)
            bolsas = BolsaPuntos.objects.filter(cliente_id=cliente_id, saldo_puntos__gt=0).order_by('fecha_asignacion')

            if not bolsas.exists():
                return Response({"error": "No hay bolsas de puntos disponibles"}, status=status.HTTP_400_BAD_REQUEST)

            # Crear la cabecera del uso de puntos
            cabecera = UsoPuntosCabecera.objects.create(
                cliente_id=cliente_id,
                puntaje_utilizado=puntaje_requerido,
                concepto_uso=concepto_uso
            )

            puntos_a_usar = int(puntaje_requerido)
            for bolsa in bolsas:
                if puntos_a_usar <= 0:
                    break

                puntos_utilizados = min(bolsa.saldo_puntos, puntos_a_usar)

                # Crear el detalle del uso de puntos
                UsoPuntosDetalle.objects.create(
                    cabecera=cabecera,
                    bolsa_puntos=bolsa,
                    puntaje_utilizado=puntos_utilizados
                )

                # Actualizar el puntaje utilizado de la bolsa
                bolsa.puntaje_utilizado += puntos_utilizados

                # Guardar la bolsa para actualizar el saldo
                bolsa.save()

                puntos_a_usar -= puntos_utilizados

            if puntos_a_usar > 0:
                return Response({"error": "No hay suficientes puntos disponibles"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(cabecera)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
