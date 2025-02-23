from flask import request, jsonify
from flask_restful import Resource
from db import db
from models.usuarios_model import UsuarioModel



class UsuariosResource(Resource):
   def post(self):
      data = request.get_json()

      # Crear un nuevo usuario
      new_user = UsuarioModel(**data)

      # Guardar el nuevo usuario en la base de datos
      db.session.add(new_user)
      db.session.commit()

      # Enviar el correo de bienvenida
      send_welcome_email(new_user.email, new_user.username)

      return jsonify({
         'mssg': 'Usuario creado exitosamente'
      })