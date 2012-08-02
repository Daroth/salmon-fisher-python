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
    ret = render_template('index.jade',
    	title='index',
    	username= '',
    	torrents=[
    		{
					'name' : 'bootstrap',
					'tags' : ['Developpement'],
					'percentage' : '85',
					'url' : '',
					'active' : 'true',
					'ratio' : 1,
					'size' : 4552,
					'contains' : []
				},
				{
					'name' : 'Die Antwoord - Tens$ion',
					'tags' : ['Musique'],
					'url' : '',
					'percentage' : '46',
					'active' : 'true',
					'ratio' : 1,
					'size' : 452452,
					'contains' : []
				},
				{
					'name' : 'Filmographie Jean Paul Rouve',
					'tags' : ['Films','Video'],
					'url' : '',
					'percentage' : '7',
					'active' : 'false',
					'ratio' : 3.9,
					'size' : '452452',
					'contains' : []
				},
				{
					'name' : 'qs454545dqsd',
					'tags' : ['Serie','Video'],
					'url' : '',
					'percentage' : '74',
					'active' : 'true',
					'ratio' : 0.12,
					'size' : 452452,
					'contains' : []
				},
				{
					'name' : 'qsd245245qsd',
					'tags' : ['test','sfsdf'],
					'url' : '',
					'percentage' : '45',
					'active' : 'false',
					'ratio' : 0.68,
					'size' : 452452,
					'contains' : []
				},
				{
					'name' : 'qsd785785qsd',
					'tags' : ['test'],
					'url' : '',
					'percentage' : '1',
					'active' : 'false',
					'ratio' : 0.46,
					'size' : 452452,
					'contains' : []
				},
				{
					'name' : 'HEY OH',
					'tags' : ['test'],
					'url' : '',
					'percentage' : '100',
					'active' : 'false',
					'ratio' : 2.01,
					'size' : 452452,
					'contains' : []
				}
			],
    	filters=[
    			{
						'name':'finished',
						'show_finished':'true',
						'show_current':'false',
						'show_paused':'false',
						'tag_filters':[]
					},
					{
						'name':'current',
						'show_finished':'false',
						'show_current':'true',
						'show_paused':'false',
						'tag_filters':[]
					},
					{
						'name':'paused',
						'show_finished':'false',
						'show_current':'false',
						'show_paused':'true',
						'tag_filters':[]
					},
					{
						'name':'tags',
						'show_finished':'true',
						'show_current':'true',
						'show_paused':'true',
						'tag_filters':[
							['video','serie'],
							['musique']
						]
					}
			]
    )
  elif request.method == 'POST':
    ret = index_post()
  return ret

@b.route('account', methods=['GET', 'POST',])
#@auth.login_required
def account():
  form = PasswordChangeForm(request.form)
  if request.method == 'GET':
    ret = render_template('user.jade',
        title='Account',
        form=form
    )
  elif request.method == 'POST':
    if form.validate():
      ret = redirect(url_for('account'))
    else:
      ret = render_template('user.jade', title='Account', form=form)
  return ret
  

