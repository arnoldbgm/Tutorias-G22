# Vamos a importar un generics
from rest_framework import generics
# Importamos el modelo
from .models import ImagenModel
# Importamos el serializador
from .serializer import ImagenSerializer
import cloudinary
from rest_framework.response import Response

# Comenzamos a crear la vista

class ImagenListCreate(generics.ListCreateAPIView):
   queryset = ImagenModel.objects.all()
   # SELECT * FROM imagenes
   serializer_class = ImagenSerializer

   # Cada que se suba una imagen
   # DNI_10036857 

   def get(self, request, *args, **kwargs):
      imagines_cloudinary = self.get_queryset()
      # SELECT * FROM imagenes
      data = []

      for obj in imagines_cloudinary:
         imagen_url = f"https://res.cloudinary.com/{cloudinary.config().cloud_name}/{obj.image}"
         
         data.append({
            'id': obj.id,
            'title': obj.title,
            'image': imagen_url
         })

      return Response(data)