from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm
#@app.route('/')
@app.route('/index')
@app.route('/login',methods=['get','post'])


def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
        title = 'Sign In',
        form = form,
		providers=app.config['OPENID_PROVIDERS'])

def index():
    user = { 'nickname': 'PeiPei' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)