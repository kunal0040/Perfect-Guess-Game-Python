import random

"""
---Perfect Guess Game---

Rules:
    > The computer will randomly select a number between 1 and 100.
    > The player will have to guess the number.
    > If the player guesses the number correctly, they win. 
    > If they guess incorrectly, they will be prompted to guess again until they get it right.
"""
print("==================================")
print("Welcome to the Perfect Guess Game!")
print("==================================")

number = random.randint(1, 100)
user_guess = -1
guesses = 0
hiscore = 0

while user_guess != number:
    try:
        user_guess = int(input("\nGuess the number: "))
        guesses += 1

        if user_guess < number:
            print("Too low! Try again.")
            if abs(number - user_guess) <= 3:
                print("You're getting close!")

        elif user_guess > number:
            print("Too high! Try again.")
            if abs(user_guess - number) <= 3:
                print("You're getting close!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


print(
    f"Congratulations!!\nYou have guessed the number {number} correctly in {guesses} guesses.")

with open("score.txt", "r") as f:
    hiscore = f.read()
    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0

if guesses < hiscore or hiscore == 0:
    print("You have set a new high score!")
    with open("score.txt", "w") as f:
        f.write(str(guesses))
