from flask import Flask
from application import views

app = Flask(__name__)

app.add_url_rule('/upload', view_func= views.upload_content, methods=['POST'])



