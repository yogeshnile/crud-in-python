from flask import Blueprint, render_template, url_for, redirect, request

auth = Blueprint('auth',__name__)

@auth.route('/singup')
def singup():
    return render_template('singup.html')

@auth.route('/singup', methods=['POST'])
def singup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    return redirect(url_for('main.profile'))

@auth.route('/logout')
def logout():
    return "used this to log out"
