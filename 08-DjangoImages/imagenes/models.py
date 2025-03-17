from django.db import models

# Create your models here.
class ImagenModel(models.Model):

   title = models.CharField(max_length=100)
   image = models.ImageField(upload_to='images/')

   class Meta:
      db_table = 'imagenes'

# MODELO 👍
# SERIALIZADOR 👍
# VISTA 👍
# URL 👍
