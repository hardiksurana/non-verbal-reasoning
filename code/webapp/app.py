from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import os
from forms import SignupForm
from flask_sqlalchemy import SQLAlchemy

# create the application object
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/turtle'
db = SQLAlchemy(app)

# Route for handling the login page logic
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if 'user already exist in database':
                return "Email address already exists"
            else:
                return "will create user here"
        else:
            return "Form didn't validate"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

if __name__ == "__main__":
    init_db()
    app.run(debug=True,port=9000)