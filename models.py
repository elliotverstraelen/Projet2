from app import db


class animaux(db.Model):
    """Data Model for animals"""

    __tablename__ = 'animals_table'
    id = db.Column(db.Integer, primary_key=True)
    famille_id = db.Column(db.Integer, unique=False, nullable = False)
    sexe = db.Column(db.String(64), unique=False, nullable = False)
    presence = db.Column(db.String(64), unique=False, nullable = False)
    apprivoise = db.Column(db.String(64), unique=False, nullable = False)
    mort_ne = db.Column(db.String(64), unique=False, nullable = False)
    decede = db.Column(db.String(64), unique=False, nullable = False)


class famillies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64), primary_key=False, nullable=False)

class types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), primary_key=False)

class animaux_types(db.Model):
    animal_id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer)
    pourcentage = db.Column(db.Float)

class velages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mere_id = db.relationship('animaux_id')
    pere_id = db.Column(db.Integer, primary_key=False, nullable=False)
    date = db.Column(db.DateTime, primary_key=False, nullable=False)

class animaux_velages(db.Model):
    animal_id = db.Column(db.Integer, primary_key=True)
    velage_id = db.Column(db.Integer, primary_key=True)

class complications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complication = db.Column(db.String(64))
class velages_complications:
    velage_id = db.Column(db.Integer, primary_key=True)
    complication_id = db.Column(db.Integer, primary_key=True)