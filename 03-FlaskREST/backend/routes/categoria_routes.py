# Vamos a crear nuestro primer endpoint de tipo POST
# Para crear nuevas categorias
# Para iniciar siempre se debe de importar el Resource

from flask_restful import Resource
from flask import request
from models.categoria_model import CategoriasTable
from db import db
# Me va a permitir GET - POST de todas mis categorias


class CategoriaListResource(Resource):
    def get(self):
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
        

    # {
    #    "nombre": "Rock"
    # }
    def post(self):
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
