from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsigniaViewSet, DesafioViewSet, ProgresoUsuarioViewSet

router = DefaultRouter()
router.register(r'insignias', InsigniaViewSet, basename='insignias')
router.register(r'desafios', DesafioViewSet, basename='desafios')
router.register(r'progresos', ProgresoUsuarioViewSet, basename='progresos')

urlpatterns = [
    path('', include(router.urls)),
]
