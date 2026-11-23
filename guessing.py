import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
secret_number = random.randint(1, 100)

if difficulty == "easy":
    global attempts
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
else:
    print("Invalid difficulty level. Please choose 'easy' or 'hard'.")

while guess != secret_number and attempts > 0:
    if guess < secret_number:
            print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess again: "))
    else:
        print("You've run out of attempts. You lose.")
        break

if guess == secret_number:
    print(f"You got it! The answer was {secret_number}.")