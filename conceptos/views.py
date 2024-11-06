from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConceptoSerializer
from .models import Concepto

# Create your views here.

class ConceptoViewSet(viewsets.ModelViewSet):
    queryset = Concepto.objects.all()
    serializer_class=ConceptoSerializer


