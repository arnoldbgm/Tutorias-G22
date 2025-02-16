from models.categoria_model import CategoriasTable
from flask import request
from db import db
# Crear un controlador
# Creando una funcion que se encargue de manejar la logica de negocio de nuestra aplicacion

def get_categorias():
    # SELECT * FROM categorias
   categorias = CategoriasTable.query.all()
   # return [ 
   #     {
   #         'id': categoria.id,
   #         'nombre': categoria.nombre
   #     }
   # for categoria in categorias]
   data = []
   for categoria in categorias:
      data.append({
            'id': categoria.id,
            'nombre': categoria.nombre
      })
   return data
        
def create_categoria():
   data = request.get_json() # Info guardada
   # Crear una instancia de tu modelo
   nueva_categoria = CategoriasTable(**data)
   # Vamos añadirlo a la bd
   db.session.add(nueva_categoria)
   db.session.commit() # Guardar en la bd
   return {
      'id': nueva_categoria.id,
      'nombre': nueva_categoria.nombre
   }, 201
