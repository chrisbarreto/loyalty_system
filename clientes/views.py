from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class=ClienteSerializer

