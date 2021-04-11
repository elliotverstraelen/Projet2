from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import os


#import views
#from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\COURS\Projet 2\projet\DataFerme.db'    #copy path de l'emplacement de la db chez vous
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Familles = Base.classes.familles
Animaux = Base.classes.animaux
Types = Base.classes.types
Animaux_types = Base.classes.animaux_types


#exemples pour visualiser les données
headings = ("animal_id,", "type_id", "pourcentage", "heritage")
data = (
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
)




#@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def table():
    type1 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 1).count()
    print(type1) #egal à 0
    type2 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 2).count()
    type3 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 3).count()
    types_name = db.session.query(Types.type).all()
    return render_template('types_pourcentage.html', type1=type1, type2=type2, type3=type3, types_name=types_name)



@app.route("/test")
def test():
    return render_template('graph.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)