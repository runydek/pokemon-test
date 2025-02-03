import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(200), nullable=False)

def init_db():
    db.create_all()

def scrape_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    response = requests.get(url)
    data = response.json()
    
    for pokemon in data['results']:
        details = requests.get(pokemon['url']).json()
        types = ", ".join([t['type']['name'] for t in details['types']])

        if not db.session.get(Pokemon, details['id']):
            new_pokemon = Pokemon(id=details['id'], name=details['name'], type=types)
            db.session.add(new_pokemon)
    
    db.session.commit()

def jsonapi_response(data, type_name):
    return {
        "data": [{
            "type": type_name,
            "id": str(pokemon.id),
            "attributes": {
                "name": pokemon.name,
                "type": pokemon.type
            }
        } for pokemon in data]
    }

@app.route("/pokemon", methods=["GET"])
def get_pokemon():
    pokemons = Pokemon.query.all()
    return jsonify(jsonapi_response(pokemons, "pokemon"))

@app.route("/pokemon/<int:pokemon_id>", methods=["GET"])
def get_pokemon_by_id(pokemon_id):
    pokemon = db.session.get(Pokemon, pokemon_id)
    if not pokemon:
        return jsonify({"errors": [{"status": "404", "title": "Not Found"}]}), 404
    return jsonify(jsonapi_response([pokemon], "pokemon"))

if __name__ == "__main__":
    with app.app_context():
        init_db()
        scrape_pokemon()
    app.run(debug=True, host="localhost", port=8000)
