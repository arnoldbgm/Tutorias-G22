# Guía de instalación y configuración 🚀

## 1. Crear un entorno virtual 🐍

```sh
python -m venv venv
```

> **Nota:** Si el comando anterior no funciona, prueba con:

```sh
python -m venv venv --without-pip
```

## 2. Activar el entorno virtual ⚡

- **En Windows (CMD o PowerShell):**
  ```sh
  venv\Scripts\activate
  ```

- **En Git Bash:**
  ```sh
  source venv/Scripts/activate
  ```

- **En macOS y Linux:**
  ```sh
  source venv/bin/activate
  ```

## 3. Instalar dependencias 🛠️

Instala Flask y las extensiones necesarias:

```sh
pip install Flask-JWT-Extended Flask-RESTful Flask-SQLAlchemy Flask-Cors
```

Para verificar la instalación:

```sh
pip list
```

---

# Configuración de la aplicación

## 1. Configuración en `app.py`

Asegúrate de configurar correctamente Flask, Flask-JWT-Extended y Flask-Cors:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

with app.app_context():
    db.create_all()
```

---

## 2. Modelo de Usuario

```python
from db import db
from sqlalchemy import Column, Integer, String

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    role = Column(String(20), default="user", nullable=False)
```

---

## 3. Ruta de registro de usuario

```python
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from flask import request
from sqlalchemy.exc import IntegrityError

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        role = data.get('role', 'user')

        if role not in ["admin", "user"]:
            return {'msg': 'Rol inválido'}, 400

        if UsuarioModel.query.filter_by(username=username).first():
            return {'msg': 'El usuario ya existe'}, 400

        hashed_password = generate_password_hash(password)
        new_user = UsuarioModel(username=username, password=hashed_password, first_name=first_name, last_name=last_name, role=role)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return {'msg': 'Usuario creado exitosamente'}, 201
        except IntegrityError:
            db.session.rollback()
            return {'msg': 'Error al registrar el usuario'}, 500
```

---

## 4. Ruta de autenticación con payload modificado

```python
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import check_password_hash
from flask import jsonify, request

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = UsuarioModel.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            additional_claims = {"role": user.role, "permissions": ["read", "write"]}
            access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1), additional_claims=additional_claims)
            refresh_token = create_refresh_token(identity=username)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        
        return jsonify({'msg': 'Credenciales incorrectas'}), 401
```

---

## 5. Ruta para refrescar el token

```python
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user, expires_delta=timedelta(hours=1))
        return jsonify(access_token=new_access_token)
```

---

## 6. Protección de rutas con JWT

```python
class Protected(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        claims = get_jwt()
        return jsonify(logged_in_as=current_user, role=claims['role'], permissions=claims['permissions'])
```

---

# Ejecución del servidor

Ejecuta la aplicación:

```sh
python app.py
```

---

## Registrar un usuario

Realiza una solicitud `POST` a `/register` con el siguiente JSON:

```json
{
    "username": "usuario",
    "password": "clave123",
    "first_name": "Nombre",
    "last_name": "Apellido",
    "role": "admin"
}
```

---

## Iniciar sesión y obtener tokens

Realiza una solicitud `POST` a `/login` con:

```json
{
    "username": "usuario",
    "password": "clave123"
}
```

Recibirás un `access_token` y un `refresh_token` en la respuesta, con un payload que incluye el `role` del usuario.

---

## Prueba la ruta protegida

Usa el `access_token` obtenido en el paso anterior y envíalo en el encabezado `Authorization` como `Bearer <token>`.

```sh
curl -H "Authorization: Bearer <token>" http://localhost:5000/protected
```

---

## Refrescar el `access_token`

Usa el `refresh_token` para obtener un nuevo `access_token`:

```sh
curl -X POST -H "Authorization: Bearer <refresh_token>" http://localhost:5000/refresh
```

---

Este README ahora está corregido, más claro y sin `Enum`. ¿Necesitas más cambios o agregar algo más? 🚀