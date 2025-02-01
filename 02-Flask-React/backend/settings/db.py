# Aqui vamos a inicializar la conexion a nuestro servidor de base de datos
# Aqui nos CONECTAMOS A LA BD 💣
from flask_sqlalchemy import SQLAlchemy

# Porque lo creo separado este settings, es porque lo vamos a usar en varios archivos

db = SQLAlchemy()