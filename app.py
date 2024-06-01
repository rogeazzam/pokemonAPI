# There are 2159 pokemons in the link: (replace {id} with a number between 1 and 2159)
# https://pokeapi.co/api/v2/item/{id}

from pokemon import Pokemon
import requests
import json
import random

first_id, last_id = 1, 2159

def main():
    backend_ip = input('Please enter the backend IP: ')
    URL = f"http://{backend_ip}:5001/mongodb"
    while True:
        draw = input("Would you like to draw a Pokemon?(yes/no): ")
        if draw != "yes":
            exit(0)
        download_ids = random.sample(range(first_id, last_id), 1)
        downloaded_pokemons = []
        for id in download_ids:
            downloaded_pokemons.append(Pokemon(f"http://pokeapi.co/api/v2/item/{str(id)}"))

        rand_ind = random.randint(0, len(downloaded_pokemons) - 1)
        selected_pokemon = downloaded_pokemons[rand_ind]

        data = {
            "database": "db_name",
            "collection": "pokemons",
            "Document": selected_pokemon.json_convertion()
        }
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url=URL, data=json.dumps(data), headers=headers)

        if r.json() == "Doesn't Exist":
            print("Doesn't Exist")
            r = requests.post(url=URL, data=json.dumps(data), headers=headers)
        print(selected_pokemon)

if __name__ == '__main__':
    main()