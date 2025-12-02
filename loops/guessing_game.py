
import random

def start():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    magic_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Make a guess (1-100): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess < magic_number:
            print("Too low. Try again!")
        elif guess > magic_number:
            print("Too high. Try again!")
        else:
            print(f"🎉 Congratulations! You've guessed the number {magic_number} in {attempts} attempts.")
            break

def main():
    while True:
        start()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
