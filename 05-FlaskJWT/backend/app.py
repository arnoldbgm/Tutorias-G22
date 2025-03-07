from flask import Flask
from db import db
from flask_restful import Api
from flask_migrate import Migrate 
from models.usuarios_model import UsuarioModel
from flask_jwt_extended import JWTManager
from routes.usuarios_routes import RegisterUser, Login, RefreshToken
from flask_cors import CORS

# Crear una instancia de flask
app = Flask(__name__)

api = Api(app)
CORS(app)
# Configuraciones 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["JWT_SECRET_KEY"] = "super-secret" 


db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Rutas de mi aplicacion
api.add_resource(RegisterUser, '/api/v1/register')
api.add_resource(Login, '/api/v1/login')
api.add_resource(RefreshToken, '/api/v1/refresh')

# Levantar mi servidor
if __name__ == '__main__':
    app.run(debug=True)