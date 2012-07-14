from main import app
from flask_peewee.admin import AdminPanel
from flask_peewee.admin import Admin
from flask_peewee.admin import ModelAdmin
from auth import auth
from model import User

admin = Admin(app, auth)

class UserAdmin(ModelAdmin):
  pass

auth.register_admin(admin)
admin.register(User, UserAdmin)
