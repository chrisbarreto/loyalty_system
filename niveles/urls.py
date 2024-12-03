from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NivelesViewSet

router=DefaultRouter()
router.register(r'niveles',NivelesViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
