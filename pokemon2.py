import csv

name = input("Enter Pokémon name: ")

with open("pokemon.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0].lower() == name.lower():
            print("Name:", row[0])
            print("Height:", row[1], "m")
            print("Weight:", row[2], "kg")
            print("Type:", row[3])
            break
    else:
        print("Pokémon not found")