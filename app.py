from flask import Flask, render_template

app = Flask(__name__)


#exemples pour visualiser les données
headings = ("animal_id,", "type_id", "pourcentage", "heritage")
data = (
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
    ("0001", "0983", "0.89", "Bb"),
)
@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')
def table():
    return render_template('heritage.html', headings=headings, data=data)




@app.route("/about")
def about():
    return render_template('about.html')
if __name__=="__main__":
    app.run(debug=True)