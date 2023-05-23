import random

top_of_range = input(
    "Please enter the maximum number of the range your guess will be in: "
)

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range < 0:
        print("Please enter a number greater than 0 the next time.")
        quit()
else:
    print("Not a digit, please enter a digit the next time.")
    quit()

guesses = 0
answer = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number.")
        continue

    if user_guess == answer:
        print("You guessed it right!")
        break
    elif user_guess > answer:
        print("Please guess lower.")
        continue
    else:
        print("Please guess higher.")
        continue

print(f"You managed to get the right answer in {guesses} guesses.")
