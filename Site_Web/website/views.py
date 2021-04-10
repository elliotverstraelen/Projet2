from flask import Blueprint, render_template  #Permet de créer des routes vers les fichiers

views = Blueprint('views', __name__)





#DATA
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


#Figure 1.1
@views.route('/q1')
def q1():
    bar_labels=labels
    bar_values=values
    return render_template('question1.html', labels=labels, values=values)

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
    return render_template('question4.html', labels=labels, values=values)

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
