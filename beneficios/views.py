from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BeneficiosSerializer
from .models import Beneficios

# Create your views here.

class BeneficiosViewSet(viewsets.ModelViewSet):
    queryset = Beneficios.objects.all()
    serializer_class=BeneficiosSerializer

