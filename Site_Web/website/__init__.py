from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CODE_SECRET' #Permet de stocker donnée de façon sûr
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataFerme.db'  

    from .views import views  #Permet de 'lier' les fichiers python entre eux 

    app.register_blueprint(views, url_prefix='/')

    return app


