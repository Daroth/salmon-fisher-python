from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for

b = Blueprint('web', __name__)

@b.route('/', methods=['GET', ])
def index():
  return render_template('index.jade', title='Index', finished=[])

