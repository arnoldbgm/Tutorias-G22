### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv
# Solo si no funciona el creado
python -m venv venv --without-pip
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


### 3. Instalar Flask 🛠️

```bash
pip install flask 
# Para verificiar si se instalao
pip list 
```

### 4. Crear un archivo `app.py` 📄
Debemos de partir creando un archivo llamado `app.py` ahi es donde es iniciara nuestro servidor

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

if __name__ == '__main__':
    app.run(debug=True)

```

### 5. Ejecutar la aplicación ▶️

```bash
# Puedo levantar mi servidor con esto
python app.py
# Tambien lo puedo levantar de esta forma
flask run

```

### 6. Configuracion de SQLAlchemy
```
pip install -U Flask-SQLAlchemy
```
> [!TIP]
> Creamos el archivo `db.py` para centralizar la instancia de `SQLAlchemy` y facilitar su importación y reutilización en diferentes partes del proyecto Flask. Esto asegura una estructura limpia y modular, permitiendo que otros módulos (como modelos o rutas) accedan a la base de datos sin redundancia en el código.

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

Ahora llamaremos a nuestro archivo `db.py` en nuestro `app.py`


```py
from flask import Flask
from db import db

# Debo ejecutarlo (instanciarlo)
app = Flask(__name__)

# Ejecutamos SQLAlchemy 
db.init_app(app)

if __name__ == '__main__':
   app.run(debug=True)
```

### 7. Conectar a una base de datos con Flask-SQLAlchemy 🔗

> [!IMPORTANT]
> Antes de poder conectarnos a la bd, debemos de tener Flask Migrate instalado y configurado

```
pip install Flask-Migrate psycopg2-binary
```

```python
from flask import Flask
from db import db
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:my_password@localhost:5432/punto_de_venta'

db.init_app(app)
migrate = Migrate(app, db)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)

if __name__ == '__main__':
    app.run(debug=True)

```
### 8. Creacion de la base de datos
![image](https://github.com/user-attachments/assets/f69a535b-f8f1-4c3b-a065-4b8f518a9f85)

### 9. Ejecutar la migración 🚀

- **Crear la carpeta `migrations` (Solo la primera vez)**:
    
    ```bash
    flask db init
    
    ```
    
- **Crear la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db migrate -m "0001-Creacion de BD"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    
    ```
    

### 10. Pasamos a crear las rutas para nuestra bd🚀

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```

---

# Ejercicios para la casa 🤓🟢

### 8. Creacion de la base de datos
![Bd](https://github.com/user-attachments/assets/4d7782ba-62e0-4148-88c9-7674e17e3d41)

### 9. Ejecutar la migración 🚀

- **Ejecutar la instancia de las migraciones**:
    
    ```bash
    flask db init
    
    ```
    
- **Crear la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db migrate -m "0001-Creacion de BD"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    ```
    

### 10. Insertaremos data dentro de nuestra bd🚀

```sql
-- Inserción de productos
INSERT INTO productos (name, price, stock) VALUES 
('Tv Samsung', 10.0, 100),
('Play Station 5', 20.0, 200),
('Moto Lineales', 30.0, 300);

-- Inserción de ventas
INSERT INTO ventas (product_id, quantity, price, timestamp) VALUES 
(1, 5, 12.0, '2024-03-05 10:00:00'),  -- Precio de venta 12.0
(2, 3, 22.0, '2024-03-10 12:00:00'),
(1, 2, 11.0, '2024-04-15 14:00:00'),
(3, 1, 33.0, '2024-04-20 16:00:00'),
(2, 4, 21.0, '2024-05-25 18:00:00'),
(1, 6, 13.0, '2024-05-30 20:00:00'),
(3, 2, 31.0, '2024-06-05 09:00:00'),
(1, 3, 12.5, '2024-06-10 11:00:00'),
(2, 5, 23.0, '2024-07-15 13:00:00'),
(3, 4, 32.0, '2024-07-20 15:00:00');

-- Inserción de compras
INSERT INTO compras (product_id, quantity, price, timestamp) VALUES 
(1, 10, 9.0, '2024-03-01 08:00:00'), 
(2, 20, 18.0, '2024-03-05 10:00:00'),
(3, 30, 27.0, '2024-03-10 12:00:00'),
(1, 15, 8.5, '2024-04-01 14:00:00'),
(2, 25, 17.5, '2024-04-05 16:00:00'),
(3, 35, 26.5, '2024-04-10 18:00:00'),
(1, 20, 9.5, '2024-05-01 08:00:00'),
(2, 30, 19.0, '2024-05-05 10:00:00'),
(3, 40, 28.0, '2024-05-10 12:00:00'),
(1, 25, 10.0, '2024-06-01 14:00:00'),
(2, 35, 20.0, '2024-06-05 16:00:00'),
(3, 45, 29.0, '2024-06-10 18:00:00'),
(1, 30, 10.5, '2024-07-01 08:00:00'),
(2, 40, 21.0, '2024-07-05 10:00:00'),
(3, 50, 30.0, '2024-07-10 12:00:00');

```

### 11. Pasamos a crear las rutas para nuestra bd🚀

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```
### Historia del POS (RETO🐍🦾)

Imaginemos que tenemos una empresa llamada **TechStore**, una tienda que vende productos tecnológicos. Un día, el jefe de la empresa, el Sr. García, entra a la oficina con una idea emocionante.

"¡Equipo, tenemos que modernizarnos!", dice el Sr. García. "Quiero que nuestro sistema de punto de venta (POS) sea más eficiente. Necesitamos una aplicación que nos permita gestionar productos, registrar ventas y compras, y además, obtener estadísticas útiles sobre nuestras transacciones. ¿Quién se anima a trabajar en esto?"

Como somos un equipo talentoso, tomamos el desafío con entusiasmo. Decidimos usar Flask, una herramienta poderosa para crear APIs en Python. A continuación, el Sr. García nos presenta diferentes retos que debemos solucionar.

### Reto 1: Listado de Productos

Primero, el Sr. García nos pide una manera de listar todos los productos disponibles en TechStore. Necesitamos crear un endpoint que nos permita obtener todos los productos desde la base de datos.

**Pregunta:** ¿Cómo podríamos crear un endpoint en Flask que liste todos los productos disponibles?

### Reto 2: Agregar un Nuevo Producto

Luego, el Sr. García nos dice que necesitamos la capacidad de agregar nuevos productos al inventario de TechStore. Necesitamos un endpoint que reciba datos de un nuevo producto y lo agregue a la base de datos.

**Pregunta:** ¿Cómo podríamos crear un endpoint en Flask que permita agregar un nuevo producto al inventario?

### Reto 3: Registrar una Venta

Para llevar el control de las ventas, el Sr. García nos pide que creemos un endpoint que registre cada venta realizada y actualice también el stock del producto vendido.

**Pregunta:** ¿Cómo podríamos crear un endpoint en Flask que registre una venta y actualice el stock del producto vendido?

### Reto 4: Registrar una Compra

Para registrar cuando adquirimos más inventario, el Sr. García quiere que añadamos un endpoint que registre las compras y actualice el stock del producto.

**Pregunta:** ¿Cómo podríamos crear un endpoint en Flask que registre una compra y actualice el stock del producto adquirido?

### Reto 5: Estadísticas de Ventas y Compras

El Sr. García también quiere ver las estadísticas mensuales de ventas y compras para tomar decisiones informadas. Nos pide crear endpoints para obtener la venta y la compra máxima por mes, así como el promedio mensual.

**Pregunta 1:** ¿Cómo podríamos crear un endpoint en Flask que obtenga la venta máxima por mes?

**Pregunta 2:** ¿Cómo podríamos crear un endpoint en Flask que calcule el promedio de ventas por mes?

**Pregunta 3:** ¿Cómo podríamos crear un endpoint en Flask que obtenga la compra máxima por mes?

**Pregunta 4:** ¿Cómo podríamos crear un endpoint en Flask que calcule el promedio de compras por mes?


