from salmon.main import app
from flaskext.script import Manager
from flaskext.script import Command

manager = Manager(app)

manager.run()

