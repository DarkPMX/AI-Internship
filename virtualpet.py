pet_name = input("What is the name of your virtual pet? ")
hunger = 5
happiness = 5

while True:
    print("\n---", pet_name, "---")
    print("Hunger:", hunger)
    print("Happiness:", happiness)


    print("\n1.Feed your pet")
    print("2.Play with your pet")
    print("3.Check status")
    print("4.Clean your pet")
    print("5.Quit")
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        hunger -= 2
        happiness += 1
        if hunger < 0:
            hunger = 0
        if hunger > 10:
            hunger = 10
        print("You fed", pet_name, "!")
    elif choice == "2":
        happiness += 2
        hunger += 1
        print("You played with", pet_name, "!")
    elif choice == "3":
        print("Status of", pet_name, ":")
        print("Hunger:", hunger)
        print("Happiness:", happiness)
    elif choice == "4":
        happiness += 1
        hunger += 2
        print("You cleaned", pet_name, "!")
    elif choice == "5":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please choose again.")
    hunger += 1
    happiness -= 1
    if hunger > 10:
        print(pet_name, "is starving! Please feed it!")
    if happiness < 0:
        print(pet_name, "is very sad! Please play with it!")
        break