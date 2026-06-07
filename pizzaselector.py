pizza = input("What size pizza do you want? (small/medium/large): ")

if pizza.lower() == "small":
    print("That's $8 please")
elif pizza.lower() == "medium":
    print("You have selected a medium pizza.")
elif pizza.lower() == "large":
    print("You have selected a large pizza for $12.")
else:
    print("Sorry, we don't have that size of pizza.")