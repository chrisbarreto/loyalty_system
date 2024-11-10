from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsoPuntosCabeceraViewSet

router = DefaultRouter()
router.register(r'usopuntos', UsoPuntosCabeceraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
