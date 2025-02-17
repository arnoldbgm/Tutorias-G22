from flask import Flask
from db import db
from flask_restful import Api
from flask_migrate import Migrate  # Es la importacion de las migraciones
from routes.categoria_routes import CategoriaListResource
from routes.post_routes import PostListResource, PostDateResource
from routes.usuarios_routes import UsuariosResource
from models.usuarios_model import UsuarioModel
from flask_mail import Mail

from flask_cors import CORS
# Crear una instancia de flask
app = Flask(__name__)
CORS(app)
api = Api(app)
# Configuraciones 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'

# Configuracion de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '<TU_EMAIL>'
app.config['MAIL_PASSWORD'] = '<TU_CONTRASEÑA>'
app.config['MAIL_DEFAULT_SENDER'] = '<TU_EMAIL>'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Rutas de mi aplicacion
api.add_resource(CategoriaListResource, '/categorias')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostDateResource, '/posts/date')
api.add_resource(UsuariosResource, '/usuarios/register')

# Levantar mi servidor
if __name__ == '__main__':
    app.run(debug=True)
