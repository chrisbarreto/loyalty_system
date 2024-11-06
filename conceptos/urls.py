from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConceptoViewSet

router=DefaultRouter()
router.register(r'conceptos',ConceptoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
