from random import randint
from poke_req import get_pokemon, get_pokemon_stats, get_random_pokemon, get_pokemon_stats_random
import time
import random

def battle_round(fighter_1: dict, fighter_2: dict) -> None:
    # stats for pokemon
    # adds defence to hp
    # states attack points

    fighter_1["hp"] += round(fighter_1["defense"] / 5, 0)
    fighter_2["hp"] += round(fighter_2["defense"] / 5, 0)



    round_count = 0
    while fighter_1["hp"] > 0 and fighter_2["hp"] > 0:
        round_count += 1
        time.sleep(0.5)


        print(f"{'='*40}")
        print(f"{'*'*17}round {round_count}{'*'*16}")
        print(f"{'=' * 40}")
        # Fighter 1 attack probability
        fighter_1_att = randint(0, fighter_1["attack"])
        fighter_2_def = randint(0, fighter_2["defense"])

        # Fighter 2 attack probability
        fighter_2_att = randint(0, fighter_2["attack"])
        fighter_1_def = randint(0, fighter_1["defense"])

        # fighter attack stats
        fighter_1_att2 = randint(1, round(fighter_1["attack"] / 4, 0))
        fighter_2_att2 = randint(1, round(fighter_2["attack"] / 4, 0))



        if fighter_1_att > fighter_2_def:
            fighter_2["hp"] -= fighter_1_att2
            print(f"{'-'*10}HIT{'-'*10}")
            print(f"{fighter_1['name']} damages {fighter_2['name']} for {fighter_1_att2} hp.")
        else:
            print(f"{'-' * 10}BLOCK{'-' * 10}")
            print(f"{fighter_2['name']} blocks {fighter_1['name']}'s attack.")
        print(f"{fighter_2['name']} has {fighter_2['hp']} hp left.")

        if fighter_2_att > fighter_1_def:
            fighter_1["hp"] -= fighter_2_att2
            print(f"{'-' * 10}HIT{'-' * 10}")
            print(f"{fighter_2['name']} damages {fighter_1['name']} for {fighter_2_att2} hp.")
        else:
            print(f"{'-' * 10}BLOCK{'-' * 10}")
            print(f"{fighter_1['name']} blocks {fighter_2['name']}'s attack.")
        print(f"{fighter_1['name']} has {fighter_1['hp']} hp left.")


def choose_fighter(player: str) -> dict:
    """Asks the user to choose a pokemon."""

    print(f"{player} choose your pokemon.")
    pokemon = get_pokemon()
    pokemon_stats = get_pokemon_stats(pokemon)
    return pokemon_stats

def choose_fighter_random(player: str) -> dict:
    """Asks the user to choose a pokemon."""

    pokemon = get_random_pokemon()
    pokemon_stats = get_pokemon_stats_random(pokemon)
    return pokemon_stats

def main() -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 20}pokemon battle game{'*' * 21}")
    print(f"{'=' * 60}")

    # Choose a character, then validate the input
    pokemon_1 = choose_fighter("Player 1")

    second_player_status = False


    while second_player_status is False:
        second_player = input("Random 2nd player y/n").lower()
        if second_player == "y":
            second_player_status = True
            pokemon_2 = choose_fighter_random("Player 2")
        elif second_player == "n":
            second_player_status = True
            pokemon_2 = choose_fighter("Player 2")
        else: second_player_status = False


    print(f"Player 1's pokemon is {pokemon_1}")
    print(f"Player 2's pokemon is {pokemon_2}")

    fighter1 = {}
    fighter2 = {}

    # Choose who goes first by comparing speeds.
    if pokemon_1["speed"] >= pokemon_2["speed"]:
        fighter1 = pokemon_1
        fighter2 = pokemon_2
    else:
        fighter1 = pokemon_2
        fighter2 = pokemon_1
    time.sleep(5)
    print("Battle begins in 3 \n")
    time.sleep(1)
    print("2 \n")
    time.sleep(1)
    print("1 \n")
    time.sleep(1)
    print("BATTLE!")
    time.sleep(1)

    # Game is a series of rounds, taking turns to attack and defend

    battle_round(fighter1, fighter2)
    print(f"\n{'='*10}BATTLE END{'='*10}")

    if fighter1["hp"] > 0:
        print(f"{fighter1['name']} WINS!")
    else:
        print(f"{fighter2['name']} WINS!")


if __name__ == "__main__":
    main()
