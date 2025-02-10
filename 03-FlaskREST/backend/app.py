from flask import Flask
from db import db
from flask_restful import Api
from flask_migrate import Migrate  # Es la importacion de las migraciones
from routes.categoria_routes import CategoriaListResource
from routes.post_routes import PostListResource
from flask_cors import CORS
# Crear una instancia de flask
app = Flask(__name__)
CORS(app)
api = Api(app)
# Configuraciones 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'

db.init_app(app)
migrate = Migrate(app, db)

# Rutas de mi aplicacion
api.add_resource(CategoriaListResource, '/categorias')
api.add_resource(PostListResource, '/posts')

# Levantar mi servidor
if __name__ == '__main__':
    app.run(debug=True)
