#Imports
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_bcrypt import Bcrypt #Used to hash password
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from forms import LoginForm
	
app = Flask(__name__)
bcrypt = Bcrypt(app)

#Config
app.config.from_object('config.DevelopmentConfig')

#Create the SQLAlchemy object
db = SQLAlchemy(app)

from models import *

#Module to make log in necessary
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

#Home 
@app.route('/')
@login_required
def home():
	users = db.session.query(User).all()
	return render_template("index.html", users=users) #Display database contents

#Welcome 
@app.route('/welcome')
def welcome():
	return render_template("Welcome.html")

#login module
@app.route('/login', methods=['GET','POST'])
def login():
	error= None
	form = LoginForm(request.form)
	if request.method=='POST':
		if form.validate_on_submit():
			error = 'Inside validate'
			user = User.query.filter_by(name=request.form['username']).first()
			if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
				session['logged_in'] = True
				flash("You are now logged in!")
				return redirect(url_for('home'))		
			else:
				error = 'Invalid credentials. Please try again.'
	return render_template('login.html', form=form, error=error)

#logout
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash("You are logged out!")
	return redirect(url_for('welcome'))

if __name__ == "__main__":
	app.run()