from rest_framework import viewsets
from .models import Insignia, Desafio, ProgresoUsuario
from .serializers import InsigniaSerializer, DesafioSerializer, ProgresoUsuarioSerializer

class InsigniaViewSet(viewsets.ModelViewSet):
    queryset = Insignia.objects.all()
    serializer_class = InsigniaSerializer

class DesafioViewSet(viewsets.ModelViewSet):
    queryset = Desafio.objects.all()
    serializer_class = DesafioSerializer

class ProgresoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ProgresoUsuario.objects.all()
    serializer_class = ProgresoUsuarioSerializer
