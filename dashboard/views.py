from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from datetime import timedelta
from django.utils.timezone import now
from clientes.models import Cliente
from usoPuntos.models import UsoPuntosCabecera, UsoPuntosDetalle
from django.db.models import Sum

class DashboardAnalyticsViewSet(ViewSet):
    """
    ViewSet para proporcionar los datos de KPIs del Dashboard Analítico.
    """

    def list(self, request):
        data = {
            'tasa_retencion': self.calcular_retencion_clientes(),
            'puntos_canjeados': self.calcular_puntos_canjeados(),
            'roi': self.calcular_roi(),
        }
        return Response(data)

    def calcular_retencion_clientes(self):
        total_clientes = Cliente.objects.count()
        print(f"Total clientes: {total_clientes}")  # Depuración

        # Asegúrate de que la relación esté correcta
        clientes_activos = Cliente.objects.filter(
            usos_puntos__fecha__gte=now() - timedelta(days=30)
        ).distinct().count()

        print(f"Clientes activos: {clientes_activos}")  # Depuración
        tasa_retencion = (clientes_activos / total_clientes) * 100 if total_clientes > 0 else 0
        return tasa_retencion

    def calcular_puntos_canjeados(self):
        puntos_canjeados = UsoPuntosCabecera.objects.aggregate(total=Sum('puntaje_utilizado'))['total'] or 0
        print(f"Puntos canjeados: {puntos_canjeados}")  # Depuración
        return puntos_canjeados

    def calcular_roi(self):
        ingresos = UsoPuntosDetalle.objects.aggregate(ingresos=Sum('puntaje_utilizado'))['ingresos'] or 0
        print(f"Ingresos: {ingresos}")  # Depuración
        costos = 1000  # Sustituir con el costo real del programa
        roi = ((ingresos - costos) / costos) * 100 if costos > 0 else 0
        return roi  # Retorna solo el valor de ROI como un número, no una tupla
