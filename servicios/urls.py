from django.urls import path
from .views import CargaPuntosView, UsoPuntosView, ConsultaEquivalenciaPuntosView

urlpatterns = [
    path('carga-puntos/', CargaPuntosView.as_view(), name='carga_puntos'),
    path('uso-puntos/', UsoPuntosView.as_view(), name='uso_puntos'),
    path('consulta-equivalencia/', ConsultaEquivalenciaPuntosView.as_view(), name='consulta_equivalencia'),
]
