from salmon import app_factory
from flaskext.script import Manager
from flaskext.script import Command

app = app_factory()
manager = Manager(app)

manager.run()

