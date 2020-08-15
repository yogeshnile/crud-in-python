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
from flask_login import LoginManager

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

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # connet to main file in flask app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #connet to auth file in flask app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app
    