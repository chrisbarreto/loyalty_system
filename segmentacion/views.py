from django.shortcuts import render
from rest_framework import viewsets
import schedule
import time
from django.http import HttpResponse
from .models import Segmentacion, Criterio, Beneficio
from .serializers import CriterioSerializer, SegmentacionSerializer, BeneficioSerializer

class SegmentacionViewSet(viewsets.ModelViewSet):
    queryset = Segmentacion.objects.all()
    serializer_class = SegmentacionSerializer

def controlar_segmentacion():
    Segmentacion.segmentar_por_edad()

def arrancar(request):
    schedule.every().day.at("20:11").do(controlar_segmentacion)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
    return HttpResponse("Segmentación realizada")


class CriterioViewSet(viewsets.ModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer


class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer

    def get_queryset(self):
        # Permite filtrar beneficios por criterio
        criterio = self.request.query_params.get('criterio', None)
        if criterio is not None:
            return self.queryset.filter(criterio=criterio)
        return self.queryset