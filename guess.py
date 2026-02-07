import random

number = random.randint(1,100)

guess = None
attempts = 0

print("🎯 Welcome to The Perfect Guess Game!")
print("Guess the number between 1 and 100")

while (guess!=number):
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
         print("Too low! Try again 🔻")
    
    elif guess > number:
         print("Too high! Try again 🔺")
    
    else:
         print("🎉 Congratulations!")
         print(f"You guessed the number {number} correctly")
         print(f"Total attempts: {attempts}")