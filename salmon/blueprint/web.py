from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_required

b = Blueprint('web', __name__)

@b.route('/', methods=['GET', ])
#@login_required
def index():
  return render_template('index.jade', title='Index', finished=[])


@b.route('/login', methods=['GET', ])
def login():
  return render_template('login.jade', title='Login')
