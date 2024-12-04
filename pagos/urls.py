from django.urls import path
from .views import SimularPagoView

urlpatterns = [
    path('simular_pago/', SimularPagoView.as_view(), name='simular_pago'),
]
