from flask_peewee.auth import Auth

from main import app, db
from model import User


auth = Auth(app, db, user_model=User)
