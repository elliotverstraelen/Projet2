from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CODE_SECRET' #Permet de stocker donnée de façon sûr


    from .views import views  #Permet de 'lier' les fichiers python entre eux 

    app.register_blueprint(views, url_prefix='/')

    return app


