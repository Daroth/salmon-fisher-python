from flask import Flask
from salmon.blueprint import web

def app_factory():
  app = Flask(__name__)

  app.config['DEBUG'] = True

  app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

  
  app.register_blueprint(web.b, url_prefix='/')
  return app
