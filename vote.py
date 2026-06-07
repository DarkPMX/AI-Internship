age=int(input("Enter your age: "))
if age > 18:
    print("You can vote.")
elif age == 18:
    print("Congratulations on reaching voting age! You can vote.")
else:
    print("You cannot vote.")