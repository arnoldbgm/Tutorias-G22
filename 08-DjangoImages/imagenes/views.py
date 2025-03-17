# Vamos a importar un generics
from rest_framework import generics
# Importamos el modelo
from .models import ImagenModel
# Importamos el serializador
from .serializer import ImagenSerializer

# Comenzamos a crear la vista

class ImagenListCreate(generics.ListCreateAPIView):
   queryset = ImagenModel.objects.all()
   # SELECT * FROM imagenes
   serializer_class = ImagenSerializer

   # Cada que se suba una imagen
   # DNI_10036857 
