from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VencimientoViewSet

router=DefaultRouter()
router.register(r'vencimientos',VencimientoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
