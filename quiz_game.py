print("Welcome to my computer quiz!")

answer = input("Do you want to play the game? ")
if answer.lower().strip() != "yes":
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does GPU stand for? ")
if answer.lower().strip() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does PSU stand for? ")
if answer.lower().strip() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does RAM stand for? ")
if answer.lower().strip() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")


print(f"You have got {str(score)} qns correct!")
print(f"You scored {str(score/4 * 100)}%.")
