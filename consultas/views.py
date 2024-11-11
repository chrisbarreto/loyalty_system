from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UsoPuntos
from .serializers import UsoPuntosSerializer
from django.utils import timezone
from bolsaPuntos.models import BolsaPuntos
from bolsaPuntos.serializers import BolsaPuntosSerializer
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework import generics
from django.db.models import Q

#Vista para uso de puntos
class UsoPuntosView(generics.CreateAPIView):
    queryset = UsoPuntos.objects.all()
    serializer_class = UsoPuntosSerializer

    def get(self, request):
        # Obtener parámetros de la consulta
        concepto_id = request.query_params.get('concepto')
        fecha = request.query_params.get('fecha')
        cliente_id = request.query_params.get('cliente')

        # Filtrar uso de puntos
        usos = UsoPuntos.objects.all()
        
        if concepto_id:
            usos = usos.filter(concepto__id=concepto_id)
        if fecha:
            usos = usos.filter(fecha__date=fecha)
        if cliente_id:
            usos = usos.filter(cliente__id=cliente_id)
        
        # Serializar los datos
        serializer = UsoPuntosSerializer(usos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Vista para consultar por bolsa de puntos
class BolsaPuntosView(generics.ListAPIView):  
    queryset = BolsaPuntos.objects.all()
    serializer_class = BolsaPuntosSerializer

    def get(self, request):
        cliente_id = request.query_params.get('cliente')
        min_puntos = request.query_params.get('min_puntos')
        max_puntos = request.query_params.get('max_puntos')

        query = Q()  #Se inicializa para la consulta

        # Filtrar por cliente si se proporciona el ID
        if cliente_id:
            query &= Q(cliente__id=cliente_id)

        # Filtrar por saldo_puntos en un rango
        if min_puntos is not None and max_puntos is not None:
            try:
                min_puntos = int(min_puntos)
                max_puntos = int(max_puntos)
                query &= Q(saldo_puntos__gte=min_puntos) & Q(saldo_puntos__lte=max_puntos)
            except ValueError:
                return Response({"error": "Los parámetros de puntos deben ser números"}, status=status.HTTP_400_BAD_REQUEST)
        elif min_puntos is not None:
            try:
                min_puntos = int(min_puntos)
                query &= Q(saldo_puntos__gte=min_puntos)
            except ValueError:
                return Response({"error": "min_puntos debe ser un número entero"}, status=status.HTTP_400_BAD_REQUEST)
        elif max_puntos is not None:
            try:
                max_puntos = int(max_puntos)
                query &= Q(saldo_puntos__lte=max_puntos)
            except ValueError:
                return Response({"error": "max_puntos debe ser un número entero"}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar las bolsas usando el objeto query
        bolsas = BolsaPuntos.objects.filter(query)

        # Serializar los resultados
        serializer = BolsaPuntosSerializer(bolsas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Vista para consultar datos de clientes con puntos vencidos
class ClientesConPuntosVencidosView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request):
        dias = request.query_params.get('dias')
        if dias:
            fecha_limite = timezone.now() + timezone.timedelta(days=int(dias))
            bolsas_vencidas = BolsaPuntos.objects.filter(fecha_caducidad__lte=fecha_limite)
            clientes_vencidos = bolsas_vencidas.values('cliente').distinct()
            clientes = Cliente.objects.filter(id__in=clientes_vencidos)
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "El parámetro 'dias' es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    

#Vista para consultar datos de clientes
class ClientesConsultaView(generics.ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()

    def get(self, request):
        nombre = request.query_params.get('nombre')
        apellido = request.query_params.get('apellido')
        cumpleaños = request.query_params.get('cumpleaños')

        query = Q() 

        # Filtrar por nombre si se proporciona
        if nombre:
            query &= Q(nombre__icontains=nombre)

        # Filtrar por apellido si se proporciona
        if apellido:
            query &= Q(apellido__icontains=apellido)

        # Filtrar por cumpleaños si se proporciona
        if cumpleaños:
            try:
                cumpleaños = timezone.datetime.strptime(cumpleaños, '%Y-%m-%d').date()
                query &= Q(fecha_nacimiento=cumpleaños)
            except ValueError:
                return Response({"error": "El parámetro 'cumpleaños' debe tener el formato YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar los clientes usando el objeto query
        clientes = self.get_queryset().filter(query)

        # Serializar los resultados
        serializer = self.get_serializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)