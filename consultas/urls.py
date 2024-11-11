# consultas/urls.py
from django.urls import path,include
from .views import UsoPuntosView, BolsaPuntosView, ClientesConPuntosVencidosView, ClientesConsultaView

urlpatterns = [
    #path('', include('consultas.urls')),
    path('uso-puntos/', UsoPuntosView.as_view(), name='uso-puntos'),
    path('bolsa-puntos/', BolsaPuntosView.as_view(), name='bolsa-puntos'),
    path('clientes-vencidos/', ClientesConPuntosVencidosView.as_view(), name='clientes-vencidos'),
    path('clientes-consulta/', ClientesConsultaView.as_view(), name='clientes-consulta'),
]