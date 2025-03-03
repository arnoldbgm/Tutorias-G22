from django.urls import path
from .views import ListarCrearCategorias

#  /categorias => Pueda insertar y leer las categorias
urlpatterns = [
   path("categorias/", ListarCrearCategorias.as_view())
]