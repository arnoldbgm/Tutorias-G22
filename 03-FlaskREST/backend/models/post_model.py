from db import db
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

class PostTable(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255))
    contenido = Column(Text)
    fecha = Column(DateTime)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
