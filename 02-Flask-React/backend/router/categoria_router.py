from flask import Blueprint

categoria_router = Blueprint('categoria_router', __name__)


# Crear un endpoint tipo POST  /categorie
# Que inserte los valores (nombre)
# Que se inserte en la bd
# Que la respuesta sea
# {
#     "id": 1,
#     "message": "Categoria creado exitosamente 👍",
#     "nombre": XXXXXXXXX
# }

@categoria_router.route('/categorie', methods=['GET'])
def create_categori():
    pass

# Crear un endpoint tipo GET /get-categories
# Que me traiga los valores (nombre)
