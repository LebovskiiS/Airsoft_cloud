from flask import render_template, request, redirect, make_response
from .token_jwt import decode_jwt
from .controllers import event_submit, events, registration_submit, login_form_submit
import sqlite3
from .token_jwt import decode_jwt


def check_jwt_view():
     token = request.cookies.get('cookies')
     decoded_token = decode_jwt(token)
     if isinstance(decoded_token, dict) and isinstance(decoded_token['id'], int):
          return redirect('/events')
     else:
          return redirect('/login/form')



def main_view():
     return render_template('main.html')



def event_form_view():
     if request.cookies.get('cookies'):
          return render_template('form_event.html')
     else:
          e = redirect('/login/form')
          return e




def event_submit_view():
     event_submit(request.form)
     return redirect('/events')


def player_form_view():
     return render_template('player_info.html')

def events_view():
     if request.cookies.get('cookies'):
          data = events()
          return render_template('events.html', event_list = data)
     else:
          e = redirect('/login/form')
          return e


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
     if token:
          resp = redirect('/events')
          resp.set_cookie(key= 'cookies', value= token, max_age=100*100*100)
          return resp
     else:
          return redirect('/login/form')

def upload_files_view():
     data = request.files