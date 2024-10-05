from flask import render_template, request, redirect, make_response
from sqlalchemy.dialects.mysql import INTEGER

from .token_jwt import create_jwt
from confg import SECRET_KEY
from .controllers import event_submit, player_submit, events, registration_submit, login_form_submit
import sqlite3
from .token_jwt import decode_jwt


def check_jwt_view():
     token = request.cookies.get('jwt')
     decoded_token = decode_jwt(token)
     if isinstance(decoded_token, dict) and isinstance(decoded_token['id'], int):
          return render_template('main.html')
     else:
          return render_template('login_form.html')



def main_view():
     return render_template('main.html')


def event_form_view():
     return render_template('form_event.html')


def event_submit_view():
     event_submit(request.form)
     return 'ok'


def player_form_view():
     return render_template('player_info.html')

def player_info_submit_view():
     player_submit(request.form)
     return 'ok'

def events_view():
     data = events()
     print(data)
     return render_template('events.html', event_list = data)



def registration_form_view():
     return render_template('registration.html')



def registration_submit_view():
     try:
          registration_submit(request.form)
          return redirect('/login/form')
     except sqlite3.IntegrityError as e:
          return f'the user already exists'


def login_form_view():
     return render_template('login_form.html')



def login_form_submit_view():
     token = login_form_submit(request.form)
     resp = make_response(redirect('/main'))
     resp.set_cookie(key= 'cookies', value= token, max_age=100*100*100, path= '/', secure=True, httponly=True )
     return resp