from flask import request, jsonify
from flask_restful import Resource
from models.post_model import PostTable
from db import db
from datetime import datetime

class PostListResource(Resource):
    def get(self):
        # SELECT * FROM posts
        # posts = PostTable.query.all()
        # localhost:5000/posts?page=1
        # El parametro que vamos a capturar se llamara page
        page = request.args.get('page', 1, type=int)
        # localhost:5000/posts?per_page=10
        # Cuantos elementos quiero mostrar por pagina per_page
        per_page = request.args.get('per_page', 10, type=int)

        # Obtener los posts ya paginados
        posts_paginate = PostTable.query.paginate(page=page, per_page=per_page, error_out=False)

        print(posts_paginate.items)

        data = []
        for post in posts_paginate.items:
            data.append({
                'id': post.id,
                'titulo': post.titulo,
                'contenido': post.contenido,
                'fecha': post.fecha.isoformat(),
            })
        print(data)
        # Ejemplo de la respuesta
        # {
        #   'total': el total de elementos que tengo en la tabla,
        #   'pages': el total de paginas que tengo,
        #   'current_page': la pagina actual en la que estoy,
        #   'per_page': cuantos elementos estoy mostrando por pagina,
        #   'data': [
        #    Listar todos los elementos que tengo 
        #   ]
        #}
        return jsonify({
            'total': posts_paginate.total,
            'pages': posts_paginate.pages,
            'current_page': posts_paginate.page,
            'per_page': posts_paginate.per_page,
            'data': data
        })

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

class PostDateResource(Resource):
    def get(self):
        # Aqui va a venir toda mi logica para poder filtrar por fechas
        # SELECT * FROM posts WHERE fecha > '2021-09-01'
        # SELECT * FROM posts WHERE fecha < '2021-09-01'
        # SELECT * FROM posts WHERE fecha > '2021-09-01' and fecha < '2021-09-30'
        
        # localhost:5000/posts/date?fecha_inicio=2021-09-01&fecha_fin=2021-09-30
        # Capturar los parametros fecha_inicio y fecha_fin
        fecha_inicio = request.args.get('fecha_inicio')
        fecha_fin= request.args.get('fecha_fin')

        try:
            if fecha_inicio:
                fecha_inicio =  datetime.fromisoformat(fecha_inicio)
            if fecha_fin:
                fecha_fin = datetime.fromisoformat(fecha_fin)
        except ValueError:
            return{
                'message': 'Formato de fecha incorrecto'
            }
        
        # Consulta con los filtros
        # SELECT * FROM posts WHERE fecha > '2021-09-01'
        # SELECT * FROM posts WHERE fecha < '2021-09-01'
        # SELECT * FROM posts WHERE fecha > '2021-09-01' and fecha < '2021-09-30'
        posts = PostTable.query.filter(
            PostTable.fecha >= fecha_inicio if fecha_inicio else True,
            PostTable.fecha <= fecha_fin if fecha_fin else True
        ).all()
        
        # data = []

        # for post in posts:
        #     data.append({
        #         'id': post.id,
        #         'titulo': post.titulo,
        #         'contenido': post.contenido,
        #         'fecha': post.fecha.isoformat(),
        #         'categoria_id': post.categoria_id
        #     })

        # return jsonify(data)

        # Vamos ahora a paginar las fechas
        # Todas las fechas las tengo guardas en posts
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        post_paginate = posts.paginate(page=page, per_page=per_page, error_out=False)

        data = []

        for post in post_paginate.items:
            data.append({
                'id': post.id,
                'titulo': post.titulo,
                'contenido': post.contenido,
                'fecha': post.fecha.isoformat(),
                'categoria_id': post.categoria_id
            })

        return jsonify({
            'total': post_paginate.total,
            'pages': post_paginate.pages,
            'current_page': post_paginate.page,
            'per_page': post_paginate.per_page,
            'data': data
        })

