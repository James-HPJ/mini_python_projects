name = input("What is your name? ")
print(f"Welcome {name}! Let's begin our adventure!")

answer = input(
    "You walk down a dark alley, and see a magic wand on the ground. Do you wish to pick it up(yes/no)?"
).lower()

if answer == "yes":
    print(
        "You have picked up a working magical wand! This might be useful against Dementors"
    )
    answer = input(
        "You see a dark shadow right around the corner of the alley, will you use a petronus spell with your wand(yes/no)?"
    ).lower()

    if answer == "yes":
        print("You banished a Dementor, you won the game!")
    elif answer == "no":
        print("A Dementor appears and rips your soul away. You lost the game!")
    else:
        print("Invalid choice, you lost the game!")

elif answer == "no":
    print("You will be defenseless against Dementors. You lose the game!")
else:
    print("Invalid choice, you lost the game.")

print("Thank you for playing the game!")
