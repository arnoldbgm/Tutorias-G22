from django.db import models


class CategoriasModel(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = "categorias"

    # Modificar __str__
    def __str__(self):
        return self.nombre

class PostModel(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True)

    categoria = models.ForeignKey(CategoriasModel,
                                  on_delete=models.CASCADE,
                                  null=True)

    class Meta:
         db_table = "posts"

    def __str__(self):
        return f"El post es {self.titulo}"