from django.urls import path
from .views import ImagenListCreate

urlpatterns = [
   path("imagenes/", ImagenListCreate.as_view())
]