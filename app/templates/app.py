from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


from app import views, models


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views
#exemples pour visualiser les données
headings = ("animal_id,", "type_id", "pourcentage", "heritage")
data = (
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
)






@app.route('/')
def table():
    return render_template('heritage.html', headings=headings, data=data)

def home():
    return render_template('home.html')





@app.route("/about")
def about():
    return render_template('about.html')
if __name__=="__main__":
    app.run(debug=True)