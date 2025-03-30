import requests
import sys
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(json.dumps({"error": "Pokémon not found"}, indent=4))
        return

    data = response.json()
    
    pokemon_info = {
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]]
    }

    print(json.dumps(pokemon_info, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python pokemon.py <pokemon_name>"}, indent=4))
        sys.exit(1)

    pokemon_name = sys.argv[1]
    fetch_pokemon_data(pokemon_name)
