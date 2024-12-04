from django.urls import path
from .views import SimularPagoView

urlpatterns = [
    path('realizar_pago/', SimularPagoView.as_view(), name='realizar_pago'),
]
