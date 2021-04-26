from flask import Blueprint, render_template  # Permet de créer des routes vers les fichiers
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
from sqlalchemy.sql import text
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
#Velages_complications = Complications.velages_collection





# ROUTES & DATA


#Routes
@views.route('/') # Il s'agit de ce qu'il y a dans l'URL, '/' veut dire pas de prefixe
def home():       #On ira donc sur la page 'home' lorsqu'il y'a '/' dans l'URL
    return render_template("home.html", labels=labels, values=values)

#Figure 1
@views.route('/q1')
def q1():
    import datetime
    def add_28(date, j):
        jour = int(date[0:2])
        mois = int(date[3:5])
        an = int(date[6:])
        day_delta = datetime.timedelta(days=28)
        start_date = datetime.datetime(an, mois, jour)
        added_date = start_date + day_delta * j
        new_jour = added_date.strftime("%d")
        new_mois = added_date.strftime("%m")
        new_an = added_date.strftime("%Y")
        return "{}/{}/{}".format(new_jour, new_mois, new_an)
    jour1 = jour2 = jour3 = jour4 = jour5 = jour6 = jour7 = jour8 = jour9 = jour10 = jour11 = jour12 = jour13 = jour14 = jour15 = jour16 = jour17 = jour18 = jour19 = jour20 = jour21 = jour22 = jour23 = jour24 = jour25 = jour26 = jour27 = jour28 = 0
    for i in range(370):
        jour1 += db.session.query(Velages).filter(Velages.date == add_28("03/11/1990", i)).count()
        jour2 += db.session.query(Velages).filter(Velages.date == add_28("04/11/1990", i)).count()
        jour3 += db.session.query(Velages).filter(Velages.date == add_28("05/11/1990", i)).count()
        jour4 += db.session.query(Velages).filter(Velages.date == add_28("06/11/1990", i)).count()
        jour5 += db.session.query(Velages).filter(Velages.date == add_28("07/11/1990", i)).count()
        jour6 += db.session.query(Velages).filter(Velages.date == add_28("08/11/1990", i)).count()
        jour7 += db.session.query(Velages).filter(Velages.date == add_28("09/11/1990", i)).count()
        jour8 += db.session.query(Velages).filter(Velages.date == add_28("10/11/1990", i)).count()
        jour9 += db.session.query(Velages).filter(Velages.date == add_28("11/11/1990", i)).count()
        jour10 += db.session.query(Velages).filter(Velages.date == add_28("12/11/1990", i)).count()
        jour11 += db.session.query(Velages).filter(Velages.date == add_28("13/11/1990", i)).count()
        jour12 += db.session.query(Velages).filter(Velages.date == add_28("14/11/1990", i)).count()
        jour13 += db.session.query(Velages).filter(Velages.date == add_28("15/11/1990", i)).count()
        jour14 += db.session.query(Velages).filter(Velages.date == add_28("16/11/1990", i)).count()
        jour15 += db.session.query(Velages).filter(Velages.date == add_28("17/11/1990", i)).count()
        jour16 += db.session.query(Velages).filter(Velages.date == add_28("18/11/1990", i)).count()
        jour17 += db.session.query(Velages).filter(Velages.date == add_28("19/11/1990", i)).count()
        jour18 += db.session.query(Velages).filter(Velages.date == add_28("20/11/1990", i)).count()
        jour19 += db.session.query(Velages).filter(Velages.date == add_28("21/11/1990", i)).count()
        jour20 += db.session.query(Velages).filter(Velages.date == add_28("22/11/1990", i)).count()
        jour21 += db.session.query(Velages).filter(Velages.date == add_28("23/11/1990", i)).count()
        jour22 += db.session.query(Velages).filter(Velages.date == add_28("24/11/1990", i)).count()
        jour23 += db.session.query(Velages).filter(Velages.date == add_28("25/11/1990", i)).count()
        jour24 += db.session.query(Velages).filter(Velages.date == add_28("26/11/1990", i)).count()
        jour25 += db.session.query(Velages).filter(Velages.date == add_28("27/11/1990", i)).count()
        jour26 += db.session.query(Velages).filter(Velages.date == add_28("28/11/1990", i)).count()
        jour27 += db.session.query(Velages).filter(Velages.date == add_28("29/11/1990", i)).count()
        jour28 += db.session.query(Velages).filter(Velages.date == add_28("30/11/1990", i)).count()
    labels = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "J14", "J15", "J16", "J17", "J18", "J19", "J20", "J21", "J22", "J23", "J24", "J25", "J26", "J27", "J28"]
    values = [jour1, jour2, jour3, jour4, jour5, jour6, jour7, jour8, jour9, jour10, jour11, jour12, jour13, jour14, jour15, jour16, jour17, jour18, jour19, jour20, jour21, jour22, jour23, jour24, jour25, jour26, jour27, jour28]
    somme  = sum(values)
    return render_template('question1.html', labels=labels, values=values, somme=somme)

#Figure 2
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
    import datetime

    dates = {}
    for i in range(13) :
        dates[i] = 0
    date_db = db.session.query(text('date')).from_statement(text('SELECT V.date FROM animaux A, velages V, animaux_velages AV where A.decede = 1 AND AV.velage_id = V.id AND AV.animal_id = A.id')).all()
    listdates = []
    for day in date_db: 
        listdates.append(datetime.datetime.strptime(repr(day), "('%d/%m/%Y',)"))
    for day in listdates:
        dates[day.timetuple().tm_mon] = dates[day.timetuple().tm_mon] + 1 
    somme = db.session.query(Animaux).filter(Animaux.decede == 1).count()
    dates.pop(0)
    return render_template('question4.html', labels=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], values=list(dates.values()), somme=somme,  type1=type1, type2=type2, type3=type3)

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

#Figure 7
@views.route('/q7')
def q7():
    bar_labels=labels
    bar_values=values
    return render_template('question7.html', labels=labels, values=values)

#add data
@views.route('/add_data')
def add_data():
    return render_template('add_data.html')
