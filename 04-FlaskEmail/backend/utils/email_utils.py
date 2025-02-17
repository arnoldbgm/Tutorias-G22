from flask_mail import Message
from flask import render_template

# to_email: Correo electronico al que se enviara el mensaje
# username: Nombre del usuario que se vera en el HTML
def send_welcome_email(to_email, username):
   from app import mail
   msg = Message('Bienvenido a nuestra aplicacion', recipients=[to_email])
   msg.html = render_template('welcome_email.html', username=username)
   mail.send(msg)