from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from clientes.models import Cliente
from bolsaPuntos.models import BolsaPuntos
from reglas.models import Reglas
from django.db import transaction

# Vista para Cargar Puntos al Cliente
class CargaPuntosView(APIView):
    def post(self, request):
        cliente_id = request.data.get('cliente')
        monto_operacion = request.data.get('monto_operacion')

        # Verificar si el cliente existe
        cliente = get_object_or_404(Cliente, id=cliente_id)

        # Obtener las reglas y aplicar la lógica de asignación de puntos
        reglas = Reglas.objects.all().order_by('limite_inferior')
        puntos_asignados = 0

        # Aplicar la regla adecuada dependiendo del monto de la operación
        for regla in reglas:
            # Si limite_superior es None, significa que no hay límite superior (regla para "de aquí en adelante")
            if regla.limite_superior is None:
                if monto_operacion >= regla.limite_inferior:
                    puntos_asignados = monto_operacion // regla.monto
                    break
            elif regla.limite_inferior <= monto_operacion <= regla.limite_superior:
                puntos_asignados = monto_operacion // regla.monto
                break

        # Si no se encontró ninguna regla aplicable, entonces asignar 0 puntos
        if puntos_asignados == 0:
            return Response({"error": "No hay reglas aplicables para este monto de operación"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear registro en BolsaPuntos
        bolsa_puntos = BolsaPuntos.objects.create(
            cliente=cliente,
            fecha_asignacion=datetime.now(),
            fecha_caducidad=datetime.now() + timedelta(days=365),  # Un año de validez como ejemplo
            puntaje_asignado=puntos_asignados,
            monto_operacion=monto_operacion
        )

        return Response({"mensaje": "Puntos cargados correctamente", "puntos_asignados": puntos_asignados}, status=status.HTTP_201_CREATED)

# Vista para Usar Puntos del Cliente
class UsoPuntosView(APIView):
    def post(self, request):
        cliente_id = request.data.get('cliente')
        concepto_uso = request.data.get('concepto_uso')
        puntaje_requerido = request.data.get('puntaje_utilizado')

        # Verificar si el cliente existe
        cliente = get_object_or_404(Cliente, id=cliente_id)

        # Obtener las bolsas de puntos del cliente ordenadas por fecha de asignación (FIFO)
        bolsas = BolsaPuntos.objects.filter(cliente=cliente, saldo_puntos__gt=0).order_by('fecha_asignacion')

        if not bolsas.exists():
            return Response({"error": "No hay bolsas de puntos disponibles"}, status=status.HTTP_400_BAD_REQUEST)

        # Usar puntos disponibles con transacción
        puntos_a_usar = puntaje_requerido
        with transaction.atomic():
            for bolsa in bolsas:
                if puntos_a_usar <= 0:
                    break

                puntos_utilizados = min(bolsa.saldo_puntos, puntos_a_usar)

                # Actualizar el puntaje utilizado y el saldo de la bolsa
                bolsa.puntaje_utilizado += puntos_utilizados
                bolsa.save()

                puntos_a_usar -= puntos_utilizados

            # Verificar si se usaron todos los puntos necesarios
            if puntos_a_usar > 0:
                return Response({"error": "No hay suficientes puntos disponibles"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"mensaje": "Puntos utilizados correctamente"}, status=status.HTTP_201_CREATED)

# Vista para Consultar la Equivalencia de Puntos según el Monto
class ConsultaEquivalenciaPuntosView(APIView):
    def get(self, request):
        monto = request.query_params.get('monto')

        if not monto:
            return Response({"error": "El parámetro 'monto' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            monto = float(monto)
        except ValueError:
            return Response({"error": "El parámetro 'monto' debe ser un número válido."}, status=status.HTTP_400_BAD_REQUEST)

        # Aplicar las reglas para determinar la equivalencia de puntos
        reglas = Reglas.objects.all().order_by('limite_inferior')
        puntos_equivalentes = 0

        for regla in reglas:
            if (regla.limite_superior is None and monto >= regla.limite_inferior) or \
               (regla.limite_inferior <= monto <= regla.limite_superior):
                puntos_equivalentes = monto // regla.monto
                break

        return Response({"monto": monto, "puntos_equivalentes": puntos_equivalentes}, status=status.HTTP_200_OK)