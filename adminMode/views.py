
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('talle')
    serializer_class = ProductoSerializer
# Create your views here.
