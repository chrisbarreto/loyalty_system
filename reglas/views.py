from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReglasSerializer
from .models import Reglas

# Create your views here.

class ReglasViewSet(viewsets.ModelViewSet):
    queryset = Reglas.objects.all()
    serializer_class=ReglasSerializer


