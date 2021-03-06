from flask import Blueprint, render_template, request # Permet de créer des routes vers les fichiers
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import text

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
    return render_template("home.html")

#Figure 1
@views.route('/velages_et_pleine_lune')
def q1():
    import datetime
    import ephem

    def cycle_pour_jour(date_string):
        """
        In: une date sous forme de string
        Out: la place du jour dans un cycle lunaire sur 28 jours
        """
        splitted_date_string = date_string.split("/")
        jour = int(splitted_date_string[0])
        mois = int(splitted_date_string[1])
        an = int(splitted_date_string[2])
        date = ephem.Date(datetime.date(an,mois,jour))
        nnm = ephem.next_new_moon(date)
        pnm = ephem.previous_new_moon(date)
        lunation = (date-pnm)/(nnm-pnm)
        return lunation*28
    
    # On extrait l'ensemble des dates de Velages
    velages_date = db.session.query(text('date')).from_statement(text('SELECT V.date FROM velages V')).all()

    # Initialisation des nbr de naissances par jour
    jour1 = jour2 = jour3 = jour4 = jour5 = jour6 = jour7 = jour8 = jour9 = jour10 = jour11 = jour12 = jour13 = jour14 = jour15 = jour16 = jour17 = jour18 = jour19 = jour20 = jour21 = jour22 = jour23 = jour24 = jour25 = jour26 = jour27 = jour28 = 0

    # Pour chaque naissance enregistrées dans la base de données, itérer le jour du cycle lunaire correspondant au jour de la naissance
    for naissance in velages_date:
        jour_du_cycle = round(cycle_pour_jour(naissance[0]))
        if jour_du_cycle == 0:
            jour28 += 1
        if jour_du_cycle == 1:
            jour1 += 1
        if jour_du_cycle == 2:
            jour2 += 1
        if jour_du_cycle == 3:
            jour3 += 1
        if jour_du_cycle == 4:
            jour4 += 1
        if jour_du_cycle == 5:
            jour5 += 1
        if jour_du_cycle == 6:
            jour6 += 1
        if jour_du_cycle == 7:
            jour7 += 1
        if jour_du_cycle == 8:
            jour8 += 1
        if jour_du_cycle == 9:
            jour9 += 1
        if jour_du_cycle == 10:
            jour10 += 1
        if jour_du_cycle == 11:
            jour11 += 1
        if jour_du_cycle == 12:
            jour12 += 1
        if jour_du_cycle == 13:
            jour13 += 1
        if jour_du_cycle == 14:
            jour14 += 1
        if jour_du_cycle == 15:
            jour15 += 1
        if jour_du_cycle == 16:
            jour16 += 1
        if jour_du_cycle == 17:
            jour17 += 1
        if jour_du_cycle == 18:
            jour18 += 1
        if jour_du_cycle == 19:
            jour19 += 1
        if jour_du_cycle == 20:
            jour20 += 1
        if jour_du_cycle == 21:
            jour21 += 1
        if jour_du_cycle == 22:
            jour22 += 1
        if jour_du_cycle == 23:
            jour23 += 1
        if jour_du_cycle == 24:
            jour24 += 1
        if jour_du_cycle == 25:
            jour25 += 1
        if jour_du_cycle == 26:
            jour26 += 1
        if jour_du_cycle == 27:
            jour27 += 1
        if jour_du_cycle == 28:
            jour28 += 1
    
    labels = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "J14", "J15", "J16", "J17", "J18", "J19", "J20", "J21", "J22", "J23", "J24", "J25", "J26", "J27", "J28"]
    values = [jour1, jour2, jour3, jour4, jour5, jour6, jour7, jour8, jour9, jour10, jour11, jour12, jour13, jour14, jour15, jour16, jour17, jour18, jour19, jour20, jour21, jour22, jour23, jour24, jour25, jour26, jour27, jour28]
    somme = sum(values)    # Total des naissances (pour calculer un %tage)
    return render_template('question1.html', labels=labels, values=values, somme=somme)

#Figure 2
@views.route('/velages_multiples_par_vaches')
def q2():

    velages_meres = db.session.query(text('mere_id')).from_statement(text('SELECT V.mere_id FROM velages V')).all()
    velages_dates = db.session.query(text('date')).from_statement(text('SELECT V.date FROM velages V')).all()

    vl_meres = []
    for p in velages_meres:
        vl_meres.append(p[0])

    vl_dates = []
    for p in velages_dates:
        vl_dates.append(p[0][6:])

    v1 = []
    v2 = []
    v3 = []
    v4 = []
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

    bar_values = [premiersVelages, deuxiemesVelages, troisiemesVelages, quatriemesVelages, cinquiemesVelages,
                  sixiemesVelages, septiemesVelages, huitiemesVelages, neuviemesVelages]

    bar_labels = ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998",
                  "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007",
                  "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                  "2017", "2018", "2019", "2020"]

    return render_template('question2.html', labels=bar_labels, values=bar_values)

#Figure 3
@views.route('/morts-nes')
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
@views.route('/deces_prematures')
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


    bar_labels=labels
    bar_values=values
    return render_template('question6.html', labels=labels, values=values)

#Figure 7
@views.route('/descendance_des_taureaux', methods=['GET', 'POST']) 
def q7():
    import datetime

    father_list_tupl = db.session.query(text('pere_id')).from_statement(text('SELECT V.pere_id FROM velages V')).all()  # Crée une liste de tuple des id des pères dans le tableau Velages
    father_list = [father_list_tupl[0][0]]
    for i in range(1, len(father_list_tupl)):    # Crée une liste des id des pères dans le tableau Velages
        if father_list_tupl[i][0] not in father_list:
            father_list.append(father_list_tupl[i][0])

    selected_father = 5002  #Initie la valeur du graphique au premier taureau
    if request.method == 'POST':
        selected_father = request.form.get('pere') # Récupère les donnée du dropdown menu

    dates_gen1 = {}
    dates_gen2 = {}
    dates_gen3 = {}
    for i in range(13):
        dates_gen1[i] = 0
        dates_gen2[i] = 0
        dates_gen3[i] = 0

    date_db = db.session.query(Velages.date).filter(Velages.pere_id == selected_father).all() # Récupère les dates des velages avec le même père

    list_dates_tot = []

    for day in date_db:
        list_dates_tot.append(datetime.datetime.strptime(repr(day), "('%d/%m/%Y',)"))  #Représente la liste des dates avec le même père sous format dd/mm/yy
    

    year_first_gen = list_dates_tot[0].timetuple().tm_year # Récupère l'année de la première génération
    list_date1 = []
    list_date2 = []
    list_date3 = []
    
    for year in list_dates_tot: 
        if year.timetuple().tm_year == year_first_gen:   # Ajoute à la liste des dates les veaux de génération 1
            list_date1.append(year)
        elif year.timetuple().tm_year == year_first_gen + 1:  # Ajoute à la liste des dates les veaux de génération 2
            list_date2.append(year)
        elif year.timetuple().tm_year == year_first_gen + 2:  # Ajoute à la liste des dates les veaux de génération 3
            list_date3.append(year)

    for day in list_date1:
        dates_gen1[day.timetuple().tm_mon] = dates_gen1[day.timetuple().tm_mon] + 1  # Pour chaque date de veaux on incrémente de 1 dans le dict des naissances par mois par génération

    for day in list_date2:
        dates_gen2[day.timetuple().tm_mon] = dates_gen2[day.timetuple().tm_mon] + 1
    
    for day in list_date3:
        dates_gen3[day.timetuple().tm_mon] = dates_gen2[day.timetuple().tm_mon] + 1

    dates_gen1.pop(0)
    dates_gen2.pop(0)
    dates_gen3.pop(0)

    

    value1 = list(dates_gen1.values()) #On récupère les valeurs du dict par génération
    value2 = list(dates_gen2.values())
    value3 = list(dates_gen3.values())

    somme1 = sum(value1) # On récupère le total des naissances par générations
    somme2 = sum(value2)
    somme3 = sum(value3)
    labels = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return render_template('question7.html', labels=labels, value1=value1, value2=value2, value3=value3, father_list=father_list, somme1=somme1, somme2=somme2, somme3=somme3, selected=selected_father)

#add data
@views.route('/test')
def test():
    return render_template('index.html')
