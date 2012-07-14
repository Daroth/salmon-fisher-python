class Configuration(object):
  DATABASE = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False,
  }
  DEBUG = False
  SECRET_KEY = 'overrites me!!!'
