from django.contrib import admin
from .models import CategoriasModel, PostModel

# Register your models here.

# Metodo 01: COmo registar en el Admin
# Primero debes de importar los modelos
# admin.site.register(CategoriasModel)
# admin.site.register(PostModel)

# Metodo 02: Como registrar en el admin
@admin.register(CategoriasModel)
# Nota: Puedes poder el nombre que desea a la clase
class CategoriasAdmin(admin.ModelAdmin):
   list_display = ["nombre"]

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
   list_display = ["titulo", "fecha", "contenido"]