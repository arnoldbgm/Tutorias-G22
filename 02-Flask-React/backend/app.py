from flask import Flask
from db import db
from flask_migrate import Migrate  # Es la importacion de las migraciones
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
# Crear una instancia de flask
app = Flask(__name__)

# Configuraciones 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'

db.init_app(app)
migrate = Migrate(app, db)

# Para crear una tabla usando SQLALchemy
class CategoriasTable(db.Model):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))

class PostTable(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255))
    contenido = Column(Text)
    fecha = Column(DateTime)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

# Levantar mi servidor
if __name__ == '__main__':
    app.run(debug=True)
