from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SegmentacionViewSet, CriterioViewSet, BeneficioViewSet

router = DefaultRouter()
router.register(r'segmentaciones', SegmentacionViewSet)
router.register(r'criterios', CriterioViewSet)
router.register(r'beneficios', BeneficioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]