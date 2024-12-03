from rest_framework import viewsets
from .serializers import PromocionSerializer 
from .models import Promocion 

# Create your views here.

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class=PromocionSerializer



