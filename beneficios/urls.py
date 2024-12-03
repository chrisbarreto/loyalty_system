from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BeneficiosViewSet

router=DefaultRouter()
router.register(r'beneficios',BeneficiosViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
