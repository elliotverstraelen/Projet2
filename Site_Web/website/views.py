from flask import Blueprint, render_template  #Permet de créer des routes vers les fichiers

views = Blueprint('views', __name__)

@views.route('/') # Il s'agit de ce qu'il y a dans l'URL, '/' veut dire pas de prefixe
def home():       #On ira donc sur la page 'home' lorsqu'il y'a '/' dans l'URL
    return render_template("home.html")