# Vamos a crear nuestro primer endpoint de tipo POST
# Para crear nuevas categorias
# Para iniciar siempre se debe de importar el Resource

from flask_restful import Resource
from flask import request
from models.categoria_model import CategoriasTable
from db import db
# Me va a permitir GET - POST de todas mis categorias
from controllers.categoria_controllers import get_categorias, create_categoria


class CategoriaListResource(Resource):
    def get(self):
        return get_categorias()
        

    # {
    #    "nombre": "Rock"
    # }
    def post(self):
        return create_categoria()