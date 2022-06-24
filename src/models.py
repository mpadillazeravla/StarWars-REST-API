from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)
    hair_color = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(120), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return '<Characters %r>' % self.Characters

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }      


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    orbital_period = db.Column(db.String(120), nullable=False)
    rotation_period = db.Column(db.String(120), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<Planets %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "climate": self.climate,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "population": self.population,
            # do not serialize the password, its a security breach
        }    