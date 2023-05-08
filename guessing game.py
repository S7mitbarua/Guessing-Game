import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

secret_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in", attempts, "attempts!")
