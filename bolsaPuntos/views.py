from django.shortcuts import render
from rest_framework import viewsets
from .models import BolsaPuntos
from .serializers import BolsaPuntosSerializer

class BolsaPuntosViewSet(viewsets.ModelViewSet):
    queryset = BolsaPuntos.objects.all()
    serializer_class = BolsaPuntosSerializer

    # Filtrar bolsas de puntos por cliente si se proporciona el parámetro en la URL
    def get_queryset(self):
        queryset = BolsaPuntos.objects.all()
        cliente_id = self.request.query_params.get('cliente_id')
        if cliente_id is not None:
            queryset = queryset.filter(cliente__id=cliente_id)
        return queryset
