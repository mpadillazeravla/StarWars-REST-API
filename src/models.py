from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favUser = db.relationship('Favorites', backref='user', lazy=True)


    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    id_character = db.Column(db.Integer, db.ForeignKey('characters.id'),nullable=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planets.id'),nullable=True)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_character": self.id_character,
            "id_planet": self.id_planet,
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
    favCharacter = db.relationship('Favorites', backref='characters', lazy=True)


    def __repr__(self):
        return f'<Characters {self.name}>'


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
    favPlanet = db.relationship('Favorites', backref='planets', lazy=True)


    def __repr__(self):
        return f'<Planets {self.planet_name}>'

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