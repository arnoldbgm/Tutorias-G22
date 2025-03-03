# Los serializadore de DRF sirven para deserealizar, validar la data, especificar que se ve a enviar o mostrar al cliente

from rest_framework import serializers
# Debes de importar a tu modelo
from .models import CategoriasModel

# Creare un serializador para categorias
class CategoriasSerializer(serializers.ModelSerializer):
   class Meta:
      model = CategoriasModel
      fields = ["nombre"]