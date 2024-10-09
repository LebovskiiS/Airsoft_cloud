from flask import Flask
from database.db import Database
from confg import TEMPLATES_FOLDER

app = Flask(__name__, template_folder= TEMPLATES_FOLDER)





app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
database = Database()
from application import routs