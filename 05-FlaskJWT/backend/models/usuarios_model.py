from db import db
from sqlalchemy import Column, Integer, String


class UsuarioModel(db.Model):
   __tablename__ = 'usuarios'
   