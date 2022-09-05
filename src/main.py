"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_jwt_extended import JWTManager
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()

  
    if not user :
        return jsonify({"msg": "datos incorrectos"}), 401


    # if email != user.email or password != user.password:
    if email != user.email or password != user.password:
        return jsonify({"msg": "datos incorrectos"}), 401 
    
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@app.route('/characters', methods=['GET'])
def obtener_characters():

    characters = Characters.query.all() 
    # Ojo porque ese Characters de arriba tiene que ir en mayus ya que llama a la class
    charactersList = list(map(lambda obj: obj.serialize(),characters))
    print(charactersList)

    # response_body = {
    #     "results": charactersList
    # }
    # Este response_body sobra porque esta creando un objeto de arrays
    # y asi es mas dificil acceder a la info

    return jsonify(charactersList), 200


@app.route('/characters/<int:characterId>', methods=['GET'])
def get_one_character(character_id):

    character = Characters.query.get(characterId) 

    return jsonify(character.serialize()), 200


@app.route('/planets', methods=['GET'])
def obtener_planets():

    planets = Planets.query.all() 
    # Ojo porque ese Characters de arriba tiene que ir en mayus ya que llama a la class
    planetsList = list(map(lambda obj: obj.serialize(),planets))

    return jsonify(planetsList), 200


@app.route('/planets/<int:planetId>', methods=['GET'])
def get_one_planet(planetId):

    planet = Planets.query.get(planetId) 

    return jsonify(planet.serialize()), 200


@app.route('/users', methods=['GET'])
def get_users():

    users = User.query.all() 
    # Ojo porque ese Characters de arriba tiene que ir en mayus ya que llama a la class
    usersList = list(map(lambda obj: obj.serialize(),users))

    return jsonify(usersList), 200


@app.route('/users/favorites', methods=['GET'])
@jwt_required()
def get_user_fav():

    userEmail = get_jwt_identity()
    user = User.query.filter_by(email=userEmail).first()
    userFavs = list(map(lambda obj: obj.serialize(),user.favUser))    

    return jsonify(userFavs), 200


@app.route("/favorite/planet/<int:planetId>", methods=["POST"])
@jwt_required()
def add_favorite_planet(planetId):

    userEmail = get_jwt_identity()
    user = User.query.filter_by(email=userEmail).first()
    planet_to_add = Planets.query.get(planetId)
 
 
    fav = Favorites(id_user=user.id, id_planet=planet_to_add.id)

    db.session.add(fav)
    db.session.commit()

    userFavs = list(map(lambda obj: obj.serialize(),user.favUser))    

    return jsonify(userFavs), 200


@app.route("/favorite/character/<int:characterId>", methods=["POST"])
@jwt_required()
def add_favorite_character(characterId):

    userEmail = get_jwt_identity()
    user = User.query.filter_by(email=userEmail).first()
    character_to_add = Characters.query.get(characterId)
 
 
    fav = Favorites(id_user=user.id, id_character=character_to_add.id)

    db.session.add(fav)
    db.session.commit()

    userFavs = list(map(lambda obj: obj.serialize(),user.favUser))    

    return jsonify(userFavs), 200


@app.route("/delete_favorite/planet/<int:planetId>", methods=["DELETE"])
@jwt_required()
def delete_favorite_planet(planetId):

    userEmail = get_jwt_identity()
    user = User.query.filter_by(email=userEmail).first()
    planet_to_del = Planets.query.get(planetId)
 
    db.session.delete(planet_to_del)
    db.session.commit()

    userFavs = list(map(lambda obj: obj.serialize(),user.favUser))    

    return jsonify(userFavs), 200


@app.route("/delete_favorite/character/<int:characterId>", methods=["DELETE"])
@jwt_required()
def delete_favorite_character(characterId):

    userEmail = get_jwt_identity()
    user = User.query.filter_by(email=userEmail).first()
    character_to_del = Characters.query.get(characterId)
 
    db.session.delete(character_to_del)
    db.session.commit()

    userFavs = list(map(lambda obj: obj.serialize(),user.favUser))    

    return jsonify(userFavs), 200
    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
