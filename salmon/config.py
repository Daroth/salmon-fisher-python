class Configuration(object):
  DATABASE = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False,
  }
  DEBUG = True
  SECRET_KEY = 'overrites me!!!'
  #BABEL_DEFAULT_LOCALE = 'fr'
  DEBUG_TB_INTERCEPT_REDIRECTS=False
