from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NivelesSerializer
from .models import Niveles
from usoPuntos.models import UsoPuntosDetalle

# Create your views here.

class NivelesViewSet(viewsets.ModelViewSet):
    queryset = Niveles.objects.all()
    serializer_class=NivelesSerializer


    