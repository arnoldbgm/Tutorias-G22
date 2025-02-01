# Primero llamamos al archivo db.py
from settings.db import db
from sqlalchemy import (Column, String, Integer, Float)


# Aqui estamos creando la tabla, y especificaremos que tienen
class CategoriasModel(db.Model):
    __tablename__ = 'categorias' # Como se llamara la tabla

        #Column(tipo)
    id = Column(Integer, primary_key=True)
    nombres = Column(String(255), nullable=False)