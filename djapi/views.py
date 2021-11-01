from rest_framework.decorators import action

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets, status
from .models import (   Documento, 
                        Categoria, 
                        SubCategoria, 
                        Producto, 
                        Proveedor,
                        ComprasDet,
                        ComprasEnc,
                        Cliente,
                        FacturaEnc,
                        FacturaDet)

from .serializer import (   DocumentoSerializer, 
                            CategoriaSerializer, 
                            SubCategoriaSerializer, 
                            ProductoSerializer, 
                            ProveedorSerializer,
                            ComprasDetSerializer,
                            ComprasSerializer,
                            ClienteSerializer,
                            FacturasDetSerializer,
                            FacturasSerializer)


def prueba(request):
    return HttpResponse('Primer Vista del Curso!')

class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Documento.objects.all().order_by('id')
    serializer_class = DocumentoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all().order_by('descripcion')
    serializer_class = CategoriaSerializer

class SubCategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubCategoria.objects.all().order_by('descripcion')
    serializer_class = SubCategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all().order_by('descripcion')
    serializer_class = ProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Proveedor.objects.all().order_by("nombre")
    serializer_class = ProveedorSerializer

class ComprasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasEnc.objects.all().order_by("id")
    serializer_class = ComprasSerializer

class ComprasDetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasDet.objects.all().order_by("id")
    serializer_class = ComprasDetSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by("nombre")
    serializer_class = ClienteSerializer

    @action(methods=['get'], detail=False,permission_classes=[],url_path='by-name/(?P<nombre>[\w\ ]+)')
    def by_name(self,request,pk=None,nombre=None):
        print(nombre)
        obj = Cliente.objects.filter(nombre__icontains=nombre,estado=True)
        if not obj:
            return Response({"detail":"No existe cliente buscado"})
        serializador = ClienteSerializer(obj,many=True)
        return Response(serializador.data)

class FacturasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FacturaEnc.objects.all().order_by("id")
    serializer_class = FacturasSerializer

class FacturaDetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FacturaDet.objects.all().order_by("id")
    serializer_class = FacturasDetSerializer

    def create(self, request):
        serializer = FacturasDetSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            print(data)
            prod = Producto.objects.get(pk=data["producto"])
            if int(prod.existencia) >= int(data["cantidad"]):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("No hay existencia suficiente")
                return Response("No hay existencia suficiente")

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        



###############################################

class Counter():

    def __init__(self):
        self.count: int = 0

    def increment(self) -> int:
        self.count += 1
        return(self.count)

counter: Counter = Counter()

#############################################

