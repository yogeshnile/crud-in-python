#############################################
#         Pushup Logger Flask-App           #
#-------------------------------------------#
#  Author   : Yogesh Nile                   #
#  Email    : yogeshnile.work4u@gmail.com   #
#  Twitter  : twitter.com/YogeshNile        #
#  GitHub   : github.com/yogeshnile         #
#############################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = SQLAlchemy()

#flask app will create app using below function
#run command 
#export FLASK_APP=(NAME OF THE FLODER) 
#flask run
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pushup_flask'

    db.init_app(app)

    # connet to main file in flask app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #connet to auth file in flask app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app
    