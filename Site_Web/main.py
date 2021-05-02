from website import create_app # On peut import website grâce __init__.py qui transforme le dossier en package
from flask_sqlalchemy import SQLAlchemy

app = create_app()

db = SQLAlchemy(app)

if __name__ == '__main__' :  #Execute la ligne seulement si on execute le fichier directement
    app.run(debug=False)  # Demarre le site

#42
