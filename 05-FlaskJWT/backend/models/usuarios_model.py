from db import db
from sqlalchemy import Column, Integer, String

class UsuarioModel(db.Model):
   __tablename__ = 'usuarios'
   
   id = Column(Integer, primary_key=True)
   username = Column(String(50), unique=True, nullable=False)
   password = Column(String(50), nullable=False)
   email = Column(String(50), unique=True, nullable=False)
   first_name = Column(String(50), nullable=False)
   last_name = Column(String(50), nullable=False)
   rol = Column(String(20), default="user", nullable=False)