from flask import Blueprint, render_template  # Permet de créer des routes vers les fichiers
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
import os

views = Blueprint('views', __name__)

from main import db
 


Base = automap_base()
Base.prepare(db.engine, reflect=True)

# Mapping de toutes les tables dans les classes
Animaux = Base.classes.animaux
Animaux_types = Base.classes.animaux_types
Complications = Base.classes.complications
Familles = Base.classes.familles
Types = Base.classes.types
Velages = Base.classes.velages

# Mapping des relations entre 2 tables
Animaux_velages = Animaux.velages_collection
Velages_complications = Complications.velages_collection





# DATA
# Importation des données SQL directement ici et les envoyer pour chaque page ?
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]





#Routes
@views.route('/') # Il s'agit de ce qu'il y a dans l'URL, '/' veut dire pas de prefixe
def home():       #On ira donc sur la page 'home' lorsqu'il y'a '/' dans l'URL
    return render_template("home.html", labels=labels, values=values)

#Figure 1
@views.route('/q1')
def q1():
    bar_labels=labels
    bar_values=values
    return render_template('question1.html', labels=labels, values=values)

#Figure 2 //DISABLED
@views.route('/q2')
def q2():
    bar_labels=labels
    bar_values=values
    return render_template('question2.html', labels=labels, values=values)

#Figure 3
@views.route('/q3')
def q3():
    bar_labels=labels
    bar_values=values
    return render_template('question3.html', labels=labels, values=values)

#Figure 4
@views.route('/q4')
def q4():
    bar_labels=labels
    bar_values=values
    type1 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 1).count()
    type2 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 2).count()
    type3 = db.session.query(Animaux_types).filter(Animaux_types.type_id == 3).count()
    types_name = db.session.query(Types.type).all()
    return render_template('question4.html', labels=labels, values=values, type1=type1, type2=type2, type3=type3)

#Figure 5
@views.route('/q5')
def q5():
    bar_labels=labels
    bar_values=values
    return render_template('question5.html', labels=labels, values=values)

#Figure 6
@views.route('/q6')
def q6():
    bar_labels=labels
    bar_values=values
    return render_template('question6.html', labels=labels, values=values)

#Figure 7 //DISABLED
@views.route('/q7')
def q7():
    bar_labels=labels
    bar_values=values
    return render_template('question7.html', labels=labels, values=values)

#add data
@views.route('/add_data')
def add_data():
    return render_template('add_data.html')
