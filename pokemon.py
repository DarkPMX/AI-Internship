import json

# Pokémon data
pokemon_data = {
    "pikachu": {
        "height": 0.4,
        "weight": 6.0,
        "type": "Electric"
    },
    "charizard": {
        "height": 1.7,
        "weight": 90.5,
        "type": "Fire/Flying"
    },
    "bulbasaur": {
        "height": 0.7,
        "weight": 6.9,
        "type": "Grass/Poison"
    }
}

# Create JSON file using json.dump()
with open("pokemon.json", "w") as file:
    json.dump(pokemon_data, file)

# User input
pokemon_name = input("Enter Pokémon name: ").lower()

# Look up Pokémon in the dictionary
if pokemon_name in pokemon_data:
    pokemon = pokemon_data[pokemon_name]

    print("\nPokémon Details")
    print("Name   :", pokemon_name.capitalize())
    print("Height :", pokemon["height"], "m")
    print("Weight :", pokemon["weight"], "kg")
    print("Type   :", pokemon["type"])
else:
    print("Pokémon not found!")