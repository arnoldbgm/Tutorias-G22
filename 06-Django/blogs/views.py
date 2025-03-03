from rest_framework import generics
from .models import CategoriasModel
from .serializers import CategoriasSerializer

# Vamos a crear la logica de nuestra vista
class ListarCrearCategorias(generics.ListCreateAPIView):
   queryset = CategoriasModel.objects.all()
   serializer_class = CategoriasSerializer