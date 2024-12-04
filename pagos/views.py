from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bolsaPuntos.models import BolsaPuntos
from clientes.models import Cliente
from reglas.models import Reglas
from django.utils import timezone
import random

class SimularPagoView(APIView):
    def post(self, request):
        # Paso 1: Recibir datos del pago
        cliente_id = request.data.get('cliente_id')
        monto = request.data.get('monto')
        metodo_pago = request.data.get('metodo_pago')  # Puede ser "Web" o "App Móvil"

        # Validar si el cliente existe
        try:
            cliente = Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Paso 2: Simulación de solicitud de pago y autorización (para pagos distintos de "Efectivo")
        if metodo_pago != 'Efectivo':
            # Simulamos un valor aleatorio para indicar si el pago es autorizado o no
            pago_autorizado = random.choice([True, False])
            if not pago_autorizado:
                return Response({"error": "Pago no autorizado por el proveedor de pagos simulado"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Paso 3: Determinar los puntos a asignar según las reglas
        reglas = Reglas.objects.all().order_by('limite_inferior')
        puntos_a_asignar = 0

        for regla in reglas:
            if regla.limite_inferior <= monto <= regla.limite_superior:
                puntos_a_asignar = monto // regla.monto  # Calcular puntos con la regla encontrada
                break

        if puntos_a_asignar == 0:
            return Response({"error": "No hay reglas aplicables para este monto de operación"}, status=status.HTTP_400_BAD_REQUEST)

        # Paso 4: Simular la confirmación y acumulación de puntos
        bolsa_puntos = BolsaPuntos.objects.create(
            cliente=cliente,
            fecha_caducidad=timezone.now() + timezone.timedelta(days=365),  # Puntos válidos por 1 año
            puntaje_asignado=puntos_a_asignar,
            puntaje_utilizado=0,
            saldo_puntos=puntos_a_asignar,
            monto_operacion=monto,
            metodo_pago=metodo_pago  # Almacenar el método de pago
        )

        # Paso 5: Responder con los resultados del proceso simulado
        return Response({
            "mensaje": "Pago realizado con éxito y puntos acumulados",
            "cliente": cliente_id,
            "puntos_acumulados": puntos_a_asignar,
            "monto_operacion": monto,
            "metodo_pago": metodo_pago,
            "estado_pago": "Pago autorizado y completado"
        }, status=status.HTTP_201_CREATED)
