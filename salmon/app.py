from flask import Flask
from flask import redirect
from flask import url_for
from salmon.blueprint import web
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('salmon.config.Configuration')
app.config.from_envvar('SALMON_LOCAL_SETTINGS', silent=True)

#debug toolbar
toolbar = DebugToolbarExtension(app)

# peewee
db = Database(app)

# template extention
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
  
# blueprint registration
app.register_blueprint(web.b, url_prefix='/')

  
