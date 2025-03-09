## Pasos para hacer deploy en Render
1. Tienes que crear una bd en (Render, AWS, AZURE, Heroku o donde deses)
2. Voy a conectar mi backend con la bd, esto lo hago desde el archivo setting.py de mi proyecto
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1"
    }
}
```
3. Vamos a instalar python-dotenv
```
pip install python-dotenv
```
4. Creamos un archivo `.env` donde colocaremos todas nuestras credenciales
```
ENGINE=XXXXXXXXXXXX
NAME=XXXXXXXXX
USER=XXXXXXXXX
PASSWORD=XXXXXXXXX
HOST=XXXXXXXXXXXXXXXX
```
5. Ahora nos vamos al `settings` y colocaremos lo siguiente:

```py
# Al inicio colocaremos 
from dotenv import load_dotenv
import os

load_dotenv()
```
6. Ahora jalaremos del archivo `.env` los valores
```py
DATABASES = {
    "default": {
        "ENGINE": os.environ["ENGINE"],
        "NAME": os.environ["NAME"],
        "USER": os.environ["USER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ["HOST"]
    }
}
```
7. Ahora permitire solicites de todos las rutas, dentro del archivo settings
```py
ALLOWED_HOSTS = ['*']
```
8. Para que se pueda ver los estilos en la pagina debemos de instalar
```
pip install whitenoise
```
9. Dentro de tu archivo `settings.py` para que tenga estilos tu admin, debes de colocar el siguiente middleware
```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
   ...
]
```

10. Dentro de mi setting al final debo de agregar
```py
STATIC_ROOT = BASE_DIR/'static'
```
11. Instalamos gunicorn
```
pip install gunicorn
```
12. Hacemos por ultimo un 
```
pip freeze > requirements.txt
```
13. Ejecutamos nuestras migraciones
```
python manage.py migrate
```
