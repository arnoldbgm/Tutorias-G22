from flask import request
from flask_restful import Resource
from models.post_model import PostTable
from db import db

class PostListResource(Resource):
    def get(self):
        # SELECT * FROM posts
        posts = PostTable.query.all()
        data = []
        for post in posts:
            data.append({
                'id': post.id,
                'titulo': post.titulo,
                'contenido': post.contenido,
                'fecha': post.fecha,
                'categoria_id': post.categoria_id
            })
        return data
    
    def post(self):
        # Siempre para un POST - PATCH - PUT
        # Se debe de utilizar request.get_json()
        data = request.get_json()
        nuevo_post = PostTable(**data)
        db.session.add(nuevo_post)
        # Siempres debes de confirmar la transaccion
        db.session.commit()
        return {
            'id': nuevo_post.id,
            'titulo': nuevo_post.titulo,
            'contenido': nuevo_post.contenido,
            'fecha': nuevo_post.fecha.isoformat(),
            'categoria_id': nuevo_post.categoria_id
        }, 201
