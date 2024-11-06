from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VencimientoSerializer
from .models import Vencimiento

# Create your views here.

class VencimientoViewSet(viewsets.ModelViewSet):
    queryset = Vencimiento.objects.all()
    serializer_class=VencimientoSerializer


