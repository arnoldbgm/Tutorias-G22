## Django + Cloudinary

### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv

```

### 2. Activar el entorno virtual ⚡
- En Windows:
    ```bash
        venv\Scripts\activate
    ```
- En gitbash:
    ```
        source venv/Scripts/activate
    ```
- En macOS y Linux:
    ```bash
        source venv/bin/activate
    ```


### 3. Instalacion de Django
```bash
pip install django
```
### 4. Crear un proyecto en Django
Con este comando crearemos nuestro primer proyecto en Django
```bash
django-admin startproject core .
```

### Instalación de Cloudinary

```sh
pip install cloudinary
```

### Configuración en Django

Edita el archivo `settings.py` y agrega `cloudinary` a las aplicaciones instaladas:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'imagenes'
]
```

### Importar y configurar Cloudinary

```python
import cloudinary
import cloudinary.uploader
import cloudinary.api
```

```python
cloudinary.config(
    cloud_name="",
    api_key="",
    api_secret=""
)
```

### Usando el ListCreateAPIView

```python
import cloudinary
from rest_framework.response import Response

class ImagenListCreate(generics.ListCreateAPIView):
   queryset = ImagenModel.objects.all()
   # SELECT * FROM imagenes
   serializer_class = ImagenSerializer

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
```

## Configuración de Imágenes en Local

Agrega la siguiente configuración en `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Configuración en `urls.py` para servir archivos de medios en desarrollo

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

