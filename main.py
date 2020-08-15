#############################################
#         Pushup Logger Flask-App           #
#-------------------------------------------#
#  Author   : Yogesh Nile                   #
#  Email    : yogeshnile.work4u@gmail.com   #
#  Twitter  : twitter.com/YogeshNile        #
#  GitHub   : github.com/yogeshnile         #
#############################################

from flask import Blueprint, render_template, url_for

#On this file all basic opration done like maitain profile, pushup etc

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')