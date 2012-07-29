import os
from salmon.main import app
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from salmon.auth import auth
from werkzeug import secure_filename
from salmon.form import PasswordChangeForm


b = Blueprint('web', __name__)

@b.context_processor
def inject_user():
  user = auth.get_logged_in_user()
  siteName = 'Salmon Fisher Torrent Manager'
  return dict(user=user, siteName=siteName)

def index_post():
  f = request.files['torrent-file']
  filename = secure_filename(f.filename)
  # TODO : adding filetype controle based on extention AND file content.
  f.save(os.path.join(app.config['TORRENTS_DIR_PATH'], filename))
  return redirect(url_for('web.index'))

@b.route('', methods=['GET', 'POST' ])
@auth.login_required
def index():
  if request.method == 'GET':
    ret = render_template('index.jade', title='Index', finished=[])
  elif request.method == 'POST':
    ret = index_post()
  return ret

@b.route('account', methods=['GET', 'POST',])
#@auth.login_required
def account():
  form = PasswordChangeForm(request.form)
  if request.method == 'GET':
    ret = render_template('user.jade', title='Account', form=form)
  elif request.method == 'POST':
    if form.validate():
      ret = redirect(url_for('account'))
    else:
      ret = render_template('user.jade', title='Account', form=form)
  return ret
