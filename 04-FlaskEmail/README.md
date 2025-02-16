# 📌 **Guía: API REST con Flask-RESTful, SQLAlchemy, Flask-Migrate y PostgreSQL**

En esta guía, crearemos una API REST en **Flask** con **Flask-RESTful**, utilizando **SQLAlchemy** para la gestión de la base de datos y **Flask-Migrate** para el control de versiones de la base de datos.

---

## **📂 Estructura del Proyecto**

Organizaremos el proyecto de manera modular para facilitar la escalabilidad y el mantenimiento:

```
/project_root
├── app.py                # Inicialización de la app y las rutas de la API
├── db.py                 # Inicialización de la base de datos
├── models/               # Carpeta para los modelos
│   ├── __init__.py
│   ├── categoria.py
│   └── post.py
├── controllers/          # Carpeta para la lógica de los controladores
│   ├── __init__.py
│   ├── categoria_controller.py
│   └── post_controller.py
├── routes/               # Carpeta para las rutas de la API
│   ├── __init__.py
│   ├── categoria_routes.py
│   └── post_routes.py
├── migrations/           # Carpeta para las migraciones
└── requirements.txt      # Dependencias del proyecto

```

---

## **1️⃣ Crear el entorno virtual e instalar dependencias**

📌 **Crear un entorno virtual:**

```bash
python -m venv venv

```

📌 **Activarlo:**

- **Windows:**
    
    ```bash
    venv\Scripts\activate
    
    ```
    
- **Git Bash/macOS/Linux:**
    
    ```bash
    source venv/bin/activate
    
    ```
    

📌 **Instalar dependencias:**

```bash
pip install flask flask-restful flask-sqlalchemy flask-migrate psycopg2

```

Si usas `requirements.txt`, agrégale:

```
flask
flask-restful
flask-sqlalchemy
flask-migrate
psycopg2

```

Y luego instala con:

```bash
pip install -r requirements.txt

```

---

## **2️⃣ Configurar la base de datos (`db.py`)**

📌 **Crear `db.py` para inicializar SQLAlchemy:**

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

---

## **3️⃣ Crear los Modelos (`models/`)**

📌 **Crear `models/categoria.py`:**

```python
from db import db
from sqlalchemy import Column, Integer, String

class CategoriasTable(db.Model):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)

```

📌 **Crear `models/post.py`:**

```python
from db import db
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

class PostTable(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)

```

---

## **4️⃣ Crear los Controladores (`controllers/`)**

📌 **Crear `controllers/categoria_controller.py`:**

```python
from flask import request
from db import db
from models.categoria import CategoriasTable

def get_categorias():
    categorias = CategoriasTable.query.all()
    return [{'id': categoria.id, 'nombre': categoria.nombre} for categoria in categorias]

def get_categoria(id):
    categoria = CategoriasTable.query.get(id)
    if categoria:
        return {'id': categoria.id, 'nombre': categoria.nombre}
    return {'message': 'Categoría no encontrada'}, 404

def create_categoria():
    data = request.get_json()
    nueva_categoria = CategoriasTable(nombre=data['nombre'])
    db.session.add(nueva_categoria)
    db.session.commit()
    return {'id': nueva_categoria.id, 'nombre': nueva_categoria.nombre}, 201

def update_categoria(id):
    data = request.get_json()
    categoria = CategoriasTable.query.get(id)
    if categoria:
        categoria.nombre = data['nombre']
        db.session.commit()
        return {'id': categoria.id, 'nombre': categoria.nombre}
    return {'message': 'Categoría no encontrada'}, 404

def delete_categoria(id):
    categoria = CategoriasTable.query.get(id)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
        return {'message': 'Categoría eliminada'}, 200
    return {'message': 'Categoría no encontrada'}, 404

```

📌 **Crear `controllers/post_controller.py`:**

```python
from flask import request
from db import db
from models.post import PostTable

def get_posts():
    posts = PostTable.query.all()
    return [{'id': post.id, 'titulo': post.titulo, 'contenido': post.contenido, 'fecha': post.fecha, 'categoria_id': post.categoria_id} for post in posts]

def get_post(id):
    post = PostTable.query.get(id)
    if post:
        return {'id': post.id, 'titulo': post.titulo, 'contenido': post.contenido, 'fecha': post.fecha, 'categoria_id': post.categoria_id}
    return {'message': 'Post no encontrado'}, 404

def create_post():
    data = request.get_json()
    nuevo_post = PostTable(
        titulo=data['titulo'],
        contenido=data['contenido'],
        fecha=data['fecha'],
        categoria_id=data['categoria_id']
    )
    db.session.add(nuevo_post)
    db.session.commit()
    return {'id': nuevo_post.id, 'titulo': nuevo_post.titulo, 'contenido': nuevo_post.contenido}, 201

def update_post(id):
    data = request.get_json()
    post = PostTable.query.get(id)
    if post:
        post.titulo = data['titulo']
        post.contenido = data['contenido']
        post.fecha = data['fecha']
        post.categoria_id = data['categoria_id']
        db.session.commit()
        return {'id': post.id, 'titulo': post.titulo, 'contenido': post.contenido}
    return {'message': 'Post no encontrado'}, 404

def delete_post(id):
    post = PostTable.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return {'message': 'Post eliminado'}, 200
    return {'message': 'Post no encontrado'}, 404

```

---

## **5️⃣ Crear las Rutas (`routes/`)**

📌 **Crear `routes/categoria_routes.py`:**

```python
from flask_restful import Resource
from controllers.categoria_controller import get_categorias, get_categoria, create_categoria, update_categoria, delete_categoria

class CategoriaListResource(Resource):
    def get(self):
        return get_categorias()

    def post(self):
        return create_categoria()

class CategoriaResource(Resource):
    def get(self, id):
        return get_categoria(id)

    def put(self, id):
        return update_categoria(id)

    def delete(self, id):
        return delete_categoria(id)

```

📌 **Crear `routes/post_routes.py`:**

```python
from flask_restful import Resource
from controllers.post_controller import get_posts, get_post, create_post, update_post, delete_post

class PostListResource(Resource):
    def get(self):
        return get_posts()

    def post(self):
        return create_post()

class PostResource(Resource):
    def get(self, id):
        return get_post(id)

    def put(self, id):
        return update_post(id)

    def delete(self, id):
        return delete_post(id)

```

---

## **6️⃣ Configurar `app.py` y ejecutar la API**

📌 **Crear `app.py`:**

```python
from flask import Flask
from flask_restful import Api
from db import db
from flask_migrate import Migrate
from routes.categoria_routes import CategoriaListResource, CategoriaResource
from routes.post_routes import PostListResource, PostResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(CategoriaListResource, '/categorias')
api.add_resource(CategoriaResource, '/categorias/<int:id>')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)

```

---

¡Con esto, tienes tu API REST bien estructurada y lista para crecer! 🚀