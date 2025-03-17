# Siempre importa los serializadores
from rest_framework import serializers
# Importa el modelo
from .models import ImagenModel

# Comenzamos a crear el serializador

class ImagenSerializer(serializers.ModelSerializer):

   class Meta:
      model = ImagenModel
      fields = '__all__'
