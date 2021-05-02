from flask import Blueprint, render_template, request  # Permet de créer des routes vers les fichiers
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
from sqlalchemy import extract
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

# Listes vide pour que les figures non modifiés continuent de fonctionner
labels = []
values = []

#Routes
@views.route('/') # Il s'agit de ce qu'il y a dans l'URL, '/' veut dire pas de prefixe
def home():       #On ira donc sur la page 'home' lorsqu'il y'a '/' dans l'URL
    return render_template("home.html")

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

    velages_id = db.session.query(text('id')).from_statement(text('SELECT V.id FROM velages V')).all()
    velages_meres = db.session.query(text('mere_id')).from_statement(text('SELECT V.mere_id FROM velages V')).all()
    velages_dates = db.session.query(text('date')).from_statement(text('SELECT V.date FROM velages V')).all()

    vl_meres = []
    for p in velages_meres:
        vl_meres.append(p[0])
    # print("vl_meres :", vl_meres)
    # print(len(vl_meres))

    vl_dates = []
    for p in velages_dates:
        vl_dates.append(p[0][6:])
    # print("vl_dates :", vl_dates)

    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []
    v5 = []
    v6 = []
    v7 = []
    v8 = []
    v9 = []

    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    d6 = []
    d7 = []
    d8 = []
    d9 = []

    for i in range(len(vl_meres)):
        if vl_meres[i] not in v1:
            v1.append(vl_meres[i])
            d1.append(vl_dates[i])
            continue
        if vl_meres[i] not in v2:
            v2.append(vl_meres[i])
            d2.append(vl_dates[i])
            continue
        if vl_meres[i] not in v3:
            v3.append(vl_meres[i])
            d3.append(vl_dates[i])
            continue
        if vl_meres[i] not in v4:
            v4.append(vl_meres[i])
            d4.append(vl_dates[i])
            continue
        if vl_meres[i] not in v5:
            v5.append(vl_meres[i])
            d5.append(vl_dates[i])
            continue
        if vl_meres[i] not in v6:
            v6.append(vl_meres[i])
            d6.append(vl_dates[i])
            continue
        if vl_meres[i] not in v7:
            v7.append(vl_meres[i])
            d7.append(vl_dates[i])
            continue
        if vl_meres[i] not in v8:
            v8.append(vl_meres[i])
            d8.append(vl_dates[i])
            continue
        if vl_meres[i] not in v9:
            v9.append(vl_meres[i])
            d9.append(vl_dates[i])
            continue

    print("v1 :", v1)
    print("len(v1) :", len(v1))
    print("d1 :", d1)
    #print("len(d1)", len(d1))
    #print("v2 :", v2)
    print("len(v2) :", len(v2))
    #print(d2)
    #print(len(d2))
    print("len(v3) :", len(v3))
    print("len(v4) :", len(v4))
    print("len(v5) :", len(v5))
    print("len(v6) :", len(v6))
    print("len(v7) :", len(v7))
    print("len(v8) :", len(v8))
    print("len(v9) :", len(v9))

    somme = len(v1) + len(v2) + len(v3) + len(v4) + len(v5) + len(v6) + len(v7) + len(v8) + len(v9)
    print("nombre velages comptabilisés dans les listes :", somme)

    premiersVelages = []
    deuxiemesVelages = []
    troisiemesVelages = []
    quatriemesVelages = []
    cinquiemesVelages = []
    sixiemesVelages = []
    septiemesVelages = []
    huitiemesVelages = []
    neuviemesVelages = []

    nbr = 0
    annee = d1[0]
    for i in range(len(d1)):
        if d1[i] == annee and i == (len(d1)-1):
            nbr += 1
            premiersVelages.append(nbr)
        elif d1[i] == annee:
            nbr += 1
        elif i == (len(d1)-1):
            premiersVelages.append(nbr)
            premiersVelages.append(1)
        else:
            premiersVelages.append(nbr)
            nbr = 1
            annee = d1[i]

    print("premiersVelages :", premiersVelages)
    print("sum(premiersVelages) :", sum(premiersVelages))
    print(len(premiersVelages))

    nbr = 0
    annee = d2[0]
    for i in range(len(d2)):
        if d2[i] == annee and i == (len(d2)-1):
            nbr += 1
            deuxiemesVelages.append(nbr)
        elif d2[i] == annee:
            nbr += 1
        elif i == (len(d2)-1):
            deuxiemesVelages.append(nbr)
            deuxiemesVelages.append(1)
        else:
            deuxiemesVelages.append(nbr)
            nbr = 1
            annee = d2[i]

    print("deuxiemesVelages :", deuxiemesVelages)
    print("sum(deuxiemesVelages) :", sum(deuxiemesVelages))
    print(len(deuxiemesVelages))

    nbr = 0
    annee = d3[0]
    for i in range(len(d3)):
        if d3[i] == annee and i == (len(d3)-1):
            nbr += 1
            troisiemesVelages.append(nbr)
        elif d3[i] == annee:
            nbr += 1
        elif i == (len(d3)-1):
            troisiemesVelages.append(nbr)
            troisiemesVelages.append(1)
        else:
            troisiemesVelages.append(nbr)
            nbr = 1
            annee = d3[i]

    print("troisiemesVelages :", troisiemesVelages)
    print("sum(troisiemesVelages) :", sum(troisiemesVelages))
    print(len(troisiemesVelages))

    nbr = 0
    annee = d4[0]
    for i in range(len(d4)):
        if d4[i] == annee and i == (len(d4)-1):
            nbr += 1
            quatriemesVelages.append(nbr)
        elif d4[i] == annee:
            nbr += 1
        elif i == (len(d4)-1):
            quatriemesVelages.append(nbr)
            quatriemesVelages.append(1)
        else:
            quatriemesVelages.append(nbr)
            nbr = 1
            annee = d4[i]
    print("quatriemesVelages :", quatriemesVelages)
    print("sum(quatriemesVelages) :", sum(quatriemesVelages))
    print(len(quatriemesVelages))

    nbr = 0
    annee = d5[0]
    for i in range(len(d5)):
        if d5[i] == annee and i == (len(d5)-1):
            nbr += 1
            cinquiemesVelages.append(nbr)
        elif d5[i] == annee:
            nbr += 1
        elif i == (len(d5)-1):
            cinquiemesVelages.append(nbr)
            cinquiemesVelages.append(1)
        else:
            cinquiemesVelages.append(nbr)
            nbr = 1
            annee = d5[i]

    print("cinquiemesVelages :", cinquiemesVelages)
    print("sum(cinquiemesVelages) :", sum(cinquiemesVelages))
    print(len(cinquiemesVelages))

    nbr = 0
    annee = d6[0]
    for i in range(len(d2)):
        if i == (len(d6)-1) and d6[i] == annee:
            nbr += 1
            sixiemesVelages.append(nbr)
            break
        elif d6[i] == annee:
            nbr += 1
        elif i == (len(d6)-1):
            sixiemesVelages.append(nbr)
            sixiemesVelages.append(1)
            break
        else:
            sixiemesVelages.append(nbr)
            nbr = 1
            annee = d6[i]

    print("sixiemesVelages :", sixiemesVelages)
    print("sum(sixiemesVelages) :", sum(sixiemesVelages))
    print(len(sixiemesVelages))

    nbr = 0
    annee = d7[0]
    for i in range(len(d2)):
        if i == (len(d7)-1) and d7[i] == annee:
            nbr += 1
            septiemesVelages.append(nbr)
            break
        elif d7[i] == annee:
            nbr += 1
        elif i == (len(d7)-1):
            septiemesVelages.append(nbr)
            septiemesVelages.append(1)
            break
        else:
            septiemesVelages.append(nbr)
            nbr = 1
            annee = d7[i]

    print("septiemesVelages :", septiemesVelages)
    print("sum(septiemesVelages) :", sum(septiemesVelages))
    print(len(septiemesVelages))

    nbr = 0
    annee = d8[0]
    for i in range(len(d2)):
        if i == (len(d8)-1) and d8[i] == annee:
            nbr += 1
            huitiemesVelages.append(nbr)
            break
        elif d8[i] == annee:
            nbr += 1
        elif i == (len(d8)-1):
            huitiemesVelages.append(nbr)
            huitiemesVelages.append(1)
            break
        else:
            huitiemesVelages.append(nbr)
            nbr = 1
            annee = d8[i]

    print("huitiemesVelages :", huitiemesVelages)
    print("sum(huitiemesVelages) :", sum(huitiemesVelages))
    print(len(huitiemesVelages))

    nbr = 0
    annee = d9[0]
    for i in range(len(d2)):
        if i == (len(d9)-1) and d9[i] == annee:
            nbr += 1
            neuviemesVelages.append(nbr)
            break
        elif d9[i] == annee:
            nbr += 1
        elif i == (len(d9)-1):
            neuviemesVelages.append(nbr)
            neuviemesVelages.append(1)
            break
        else:
            neuviemesVelages.append(nbr)
            nbr = 1
            annee = d9[i]

    print("neuviemesVelages :", neuviemesVelages)
    print("sum(neuviemesVelages) :", sum(neuviemesVelages))
    print(len(neuviemesVelages))

    bar_values = [premiersVelages, deuxiemesVelages, troisiemesVelages, quatriemesVelages, cinquiemesVelages,
                  sixiemesVelages, septiemesVelages, huitiemesVelages, neuviemesVelages]

    # for i in range(31):
    #    bar_values[i] = [velages_1, velages_2, velages_3, velages_4, velages_5, velages_6, velages_7, velages_8,
    #                    velages_9, velages_10]

    date_db = db.session.query(text('date')).from_statement(text('SELECT V.date FROM velages V')).all()

    bar_labels = ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998",
                  "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007",
                  "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                  "2017", "2018", "2019", "2020"]

    return render_template('question2.html', labels=bar_labels, values=bar_values)





#Figure 3
@views.route('/q3')
def q3():
    #3.1
    import datetime
    
    dates = {}
    for i in range(13) :
        dates[i] = 0
    date_db = db.session.query(text('date')).from_statement(text('SELECT V.date FROM animaux A, velages V, animaux_velages AV where A.mort_ne = 1 AND AV.velage_id = V.id AND AV.animal_id = A.id')).all()
    listdates = []
    for day in date_db: 
        listdates.append(datetime.datetime.strptime(repr(day), "('%d/%m/%Y',)"))
    for day in listdates:
        dates[day.timetuple().tm_mon] = dates[day.timetuple().tm_mon] + 1 
    somme = db.session.query(Animaux).filter(Animaux.mort_ne == 1).count()
    dates.pop(0)
    return render_template('question3.html', labels=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], values=list(dates.values()), somme = somme)

#Figure 4
@views.route('/q4')
def q4():
    import datetime

    dates = {}
    for i in range(13):
        dates[i] = 0
    date_db = db.session.query(text('date')).from_statement(text('SELECT V.date FROM animaux A, velages V, animaux_velages AV where A.decede = 1 AND AV.velage_id = V.id AND AV.animal_id = A.id')).all()
    listdates = []
    for day in date_db: 
        listdates.append(datetime.datetime.strptime(repr(day), "('%d/%m/%Y',)"))
    for day in listdates:
        dates[day.timetuple().tm_mon] = dates[day.timetuple().tm_mon] + 1
    somme = db.session.query(Animaux).filter(Animaux.decede == 1).count()
    dates.pop(0)
    return render_template('question4.html', labels=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], values=list(dates.values()), somme=somme)

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
    import datetime

    father_list_tupl = db.session.query(text('pere_id')).from_statement(text('SELECT V.pere_id FROM velages V')).all()
    father_list = [father_list_tupl[0][0]]
    for i in range(1, len(father_list_tupl)):
        if father_list_tupl[i][0] not in father_list:
            father_list.append(father_list_tupl[i][0])

    

    dates_gen1 = {}
    dates_gen2 = {}
    dates_gen3 = {}
    for i in range(13):
        dates_gen1[i] = 0
        dates_gen2[i] = 0
        dates_gen3[i] = 0

    date_db = db.session.query(text('date')).from_statement(text('SELECT V.date FROM velages V WHERE V.pere_id = 5005')).all()

    list_dates_tot = []

    for day in date_db:
        list_dates_tot.append(datetime.datetime.strptime(repr(day), "('%d/%m/%Y',)"))  #represente la date sous le format dd/mm/yy
    

    year_first_gen = list_dates_tot[0].timetuple().tm_year
    list_date1 = []
    list_date2 = []
    list_date3 = []
    for year in list_dates_tot:
        if year.timetuple().tm_year == year_first_gen:
            list_date1.append(year)
        elif year.timetuple().tm_year == year_first_gen + 1:
            list_date2.append(year)
        elif year.timetuple().tm_year == year_first_gen + 2:
            list_date3.append(year)

    for day in list_date1:
        dates_gen1[day.timetuple().tm_mon] = dates_gen1[day.timetuple().tm_mon] + 1

    for day in list_date2:
        dates_gen2[day.timetuple().tm_mon] = dates_gen2[day.timetuple().tm_mon] + 1
    
    for day in list_date3:
        dates_gen3[day.timetuple().tm_mon] = dates_gen2[day.timetuple().tm_mon] + 1

    dates_gen1.pop(0)
    dates_gen2.pop(0)
    dates_gen3.pop(0)

    

    value1 = list(dates_gen1.values())
    value2 = list(dates_gen2.values())
    value3 = list(dates_gen3.values())

    somme1 = sum(value1)
    somme2 = sum(value2)
    somme3 = sum(value3)
    labels = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return render_template('question7.html', labels=labels, values=values, value1=value1, value2=value2, value3=value3, father_list=father_list, somme1=somme1, somme2=somme2, somme3=somme3)

#add data
@views.route('/add_data')
def add_data():
    return render_template('add_data.html')
