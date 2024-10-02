import random

random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < random_number:
        print("Your guess is too low!")
    elif guess > random_number:
        print("Your guess is too high!")
    else:
        print(f"Congratulations! You guessed the right number, {random_number}, in {attempts} attempts.")
        break

print("Thanks for playing!")
