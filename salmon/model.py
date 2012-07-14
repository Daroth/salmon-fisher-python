from flask_peewee.auth import BaseUser
from main import db
from peewee import CharField
from peewee import BooleanField

class User(db.Model, BaseUser):
  username=CharField()
  password=CharField()
  active=BooleanField(default=True)
  admin=BooleanField(default=False)
  
  def __unicode__(self):
    return self.username

def create_tables():
  User.create_table()
