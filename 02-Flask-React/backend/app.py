from flask import Flask
from settings.db import db 
from flask_migrate import Migrate
from flask_cors import CORS
# Para que te reconzca la bd debes de importarlo de esta forma 🐍
from models import (
    categoria_model,
    post_model
)
from router.categoria_router import categoria_router
# Estoy importando el post router
from router.post_router import post_router


app = Flask(__name__)
CORS(app)
# Aqui va las credenciales de mi bd                   #usuario:contr@localhost:#puerto/#nombrebd
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/db_pos"

# Aqui le digo que cuanto inicie mi app, que se haga la migracion si es que hay
db.init_app(app)
migrate = Migrate(app, db)

# Aqui es donde voy a crear mi ruta
app.register_blueprint(categoria_router, url_prefix='/api/v1')
app.register_blueprint(post_router, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
