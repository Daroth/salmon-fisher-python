from flask import Flask
from salmon.blueprint import web
from flask_debugtoolbar import DebugToolbarExtension

def app_factory():
  app = Flask(__name__)

  app.config['DEBUG'] = True
  app.config['SECRET_KEY'] = '<replace with a secret key>'


  toolbar = DebugToolbarExtension(app)

  app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
  
  app.register_blueprint(web.b, url_prefix='/')
  return app
