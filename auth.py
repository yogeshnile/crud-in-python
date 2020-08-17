#############################################
#         Pushup Logger Flask-App           #
#-------------------------------------------#
#  Author   : Yogesh Nile                   #
#  Email    : yogeshnile.work4u@gmail.com   #
#  Twitter  : twitter.com/YogeshNile        #
#  GitHub   : github.com/yogeshnile         #
#############################################

from flask import Blueprint, render_template, url_for, redirect, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required, current_user

#On this file all auth opration done like singup, login, logout etc

auth = Blueprint('auth',__name__)

@auth.route('/singup')
def singup():
    return render_template('singup.html')

@auth.route('/singup', methods=['POST'])
def singup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/profile', methods=['POST'])
@login_required
def profile_post():
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    repate_password = request.form.get('repate_password')

    if new_password != repate_password:
        flash('New password and Repate password Does not match')
        return redirect(url_for('main.profile'))
    else:
        user_pass = User.query.filter_by(email=current_user.email).first()
        
        if check_password_hash(user_pass.password, current_password):
            user_pass.password = generate_password_hash(new_password, method='sha256')
            db.session.commit()
            return redirect(url_for('auth.logout'))
        else:
            flash('You entered worng password')
            return redirect(url_for('main.profile'))
