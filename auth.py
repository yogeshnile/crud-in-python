from flask import Blueprint, render_template, url_for

auth = Blueprint('auth',__name__)

@auth.route('/singup')
def singup():
    return render_template('singup.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "used this to log out"
