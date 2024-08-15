from flask_sqlalchemy import SQLAlchemy
from config.constants import *

def connect(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_DRIVER + "://" + DATABASE_USER + ":" + DATABASE_PASSWORD + "@" + DATABASE_HOST + ":3306/" + DATABASE_NAME
    db = SQLAlchemy(app)
    return db