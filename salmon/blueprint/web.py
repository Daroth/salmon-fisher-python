from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from salmon.auth import auth


b = Blueprint('web', __name__)

@b.context_processor
def inject_user():
  user = auth.get_logged_in_user()
  return dict(user=user)

@b.route('/', methods=['GET', ])
@auth.login_required
def index():
  return render_template('index.jade', title='Index', finished=[])


@b.route('/about', methods=['GET', ])
def about():
  return render_template('about.jade', title='About')

