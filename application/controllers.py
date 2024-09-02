from application import exeptions
from data_base import db
from flask import request
from . import exeptions


def upload():
    data = request.json
    data_base = db.Database()
    if data:
        data_base.insert_one(data)
    else:
        print('empty dictionary')
        raise exeptions.No_data()





