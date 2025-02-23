from flask import Flask
from db import db
from flask_restful import Api
from flask_migrate import Migrate 


# Crear una instancia de flask
app = Flask(__name__)

api = Api(app)
# Configuraciones 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'
db.init_app(app)
migrate = Migrate(app, db)

# Rutas de mi aplicacion


# Levantar mi servidor
if __name__ == '__main__':
    app.run(debug=True)
