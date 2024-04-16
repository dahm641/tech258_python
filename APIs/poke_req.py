import requests
import json
import random


def get_pokemon() -> dict:
    # choose pokemon and validate with server
    poke_req = None

    valid_pokemon = False

    while valid_pokemon is False:

        pokemon_name = input("Please enter pokemon name: ").lower()
        # pokemon name is case sensitive
        poke_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

        if poke_req.status_code == 200:
            valid_pokemon = True
        elif poke_req.status_code == 404:
            print(f"error {pokemon_name} is not a valid pokemon! try again")
        else:
            print(poke_req.status_code)

    return poke_req.json()


def get_pokemon_stats(pokemon: dict):
    pokemon_stats = {
        "name": pokemon["name"]
    }
    # pokemon dictionary from before. we want to get values from the list ffrom the key "stats"
    for stat in pokemon["stats"]:
        # Get stat_name and stat_value
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        # Add key and value to pokemon_stats dict.
        pokemon_stats[stat_name] = stat_value


    return pokemon_stats


def get_random_pokemon() -> dict:
    poke_req_random = {}
    valid_pokemon = False
    while not valid_pokemon:
        pokemon_id = random.randint(1, 1000)
        poke_req_random = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        if poke_req_random.status_code == 200:
            valid_pokemon = True

        elif poke_req_random.status_code == 404:
            print(f"ERROR! {pokemon_id} is not a valid pokemon")
            print(f"API STATUS CODE: 404")
        elif poke_req_random.status_code == 500:
            print("API NOT AVAILABLE")
            print(f"API STATUS CODE: 500")
        else:

            print(poke_req_random.status_code)
    return poke_req_random.json()


def get_pokemon_stats_random(pokemon: dict) -> dict:
    pokemon_stats = {
        "name": pokemon["name"]
    }

    for stat in pokemon["stats"]:
        # Get stat_name and stat_value
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        # Add key and value to pokemon_stats dict.
        pokemon_stats[stat_name] = stat_value

    return pokemon_stats

