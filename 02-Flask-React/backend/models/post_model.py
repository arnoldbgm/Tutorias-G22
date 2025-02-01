from settings.db import db
from sqlalchemy import (Column, 
                        String, 
                        Integer, 
                        ForeignKey, 
                        Text, 
                        DateTime)


class PostModel(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    titulo = Column(String, nullable=False)
    contenido = Column(Text, nullable=False)
    #                              ForeignKey( nombre_tabla.columna)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))