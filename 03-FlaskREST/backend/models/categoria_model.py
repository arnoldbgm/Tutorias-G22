from db import db
from sqlalchemy import Column, Integer, String

class CategoriasTable(db.Model):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))