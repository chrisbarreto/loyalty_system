from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReglasViewSet

router=DefaultRouter()
router.register(r'reglas',ReglasViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
