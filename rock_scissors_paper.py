import random

user_wins = 0
computer_wins = 0

options = ["rock", "scissors", "paper"]

while True:
    user_choice = input("Enter Rock/Scissors/Paper or Q to quit: ").lower()

    if user_choice == "q":
        print("You have chosen to quit. See you the next time!")
        break
    elif user_choice not in options:
        print("Please enter a valid option(Rock/Scissors/Paper): ")
        continue

    random_choice = random.randint(0, 2)
    computer_choice = options[random_choice]
    print("The computer chose", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You won!")
    elif user_choice == computer_choice:
        print("It is a draw.")
    else:
        computer_wins += 1
        print("The computer won.")

print(f"The user scored {user_wins} points")
print(f"The computer scored {computer_wins} points")
