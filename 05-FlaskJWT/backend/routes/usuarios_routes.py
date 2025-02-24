from flask import request, jsonify
from flask_restful import Resource
from db import db
from models.usuarios_model import UsuarioModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class RegisterUser(Resource):
   def post(self):
      # El frontend va enviar un json con los datos del usuario
      # {
      # username : "arnoldg"
      # password : "123456"
      # email: "a@a.com"
      # first_name: "Arnold"
      # last_name : "Gonzalez"
      # rol: "superusuario"
      # }
      data = request.get_json()
      username = data.get("username")
      password = data.get("password")
      email = data.get("email")
      first_name = data.get("first_name")
      last_name = data.get("last_name")
      rol = data.get("rol", "user")

      if rol not in ["user", "admin", "superuser"]:
         return {"message": "El rol no es valido"}, 400
      
      # Verificar si el usuario ya existe
      if UsuarioModel.query.filter_by(username=username).first():
         return {"message": "El usuario ya existe"}, 400
      
      # Encriptar la contraseña
      password = generate_password_hash(password)

      # Crear un nuevo usuario
      new_user = UsuarioModel(username=username,
                   password=password, 
                   email=email, 
                   first_name=first_name, 
                   last_name=last_name, 
                   rol=rol)
      
      db.session.add(new_user)
      db.session.commit()

      return {
         "msg": "Usuario creado exitosamente"
      }, 201
   
# Vamos a crear un endpoint para el access token
# Este access se genera cuando el usuario se loguea

class Login(Resource):
   def post(self):
      # El frontend va enviar un json con los datos del usuario
      # {
      # username : "arnoldg"
      # password : "123456"
      # }
      data = request.get_json()
      username = data.get("username")
      password = data.get("password")

      # Buscar el usuario en la base de datos
      user = UsuarioModel.query.filter_by(username=username).first()

      if user and check_password_hash(user.password, password):
         # Creamos nuestra access token
         # Access token dura 30 dias
         access_token = create_access_token(
                                          identity=username, 
                                          expires_delta=timedelta(days=30))
         # Creamos el refresh token
         # Refresh token dura 90 dias
         resfresh_token = create_refresh_token(
                                          identity=username,
                                          expires_delta=timedelta(days=90))
         
         return jsonify(
                        access_token=access_token, 
                        refresh_token=resfresh_token)