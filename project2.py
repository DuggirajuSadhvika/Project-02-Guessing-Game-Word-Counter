
import random
import string
from collections import Counter


def number_guessing_game():
    best_score = 0

    while True:
        secret_number = random.randint(1, 100)
        attempts = 5
        score = 100
        won = False

        print("\n===== NUMBER GUESSING GAME =====")
        print("Guess a number between 1 and 100")
        print("You have 5 attempts.")

        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("Enter a number between 1 and 100.")
                    continue

                attempts -= 1

                if guess == secret_number:
                    print("Correct! You won!")
                    print("Your score:", score)
                    won = True
                    break
                elif guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")

                score -= 10
                print("Attempts remaining:", attempts)

            except ValueError:
                print("Invalid input! Enter a whole number.")

        if not won:
            print("Game over!")
            print("The secret number was:", secret_number)
            print("Your score: 0")

        if won and score > best_score:
            best_score = score
            print("New best score!")

        print("Best score:", best_score)

        play_again = input("Play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thank you for playing!")
            break


def word_counter():
    try:
        with open("sample.txt", "r", encoding="utf-8") as file:
            text = file.read()

        text = text.lower()
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        words = text.split()
        word_counts = Counter(words)

        print("\n===== WORD COUNTER =====")
        print("Total words:", len(words))
        print("Unique words:", len(word_counts))

        print("\nTop 10 common words:")
        for word, count in word_counts.most_common(10):
            print(word, ":", count)

    except FileNotFoundError:
        print("Error: sample.txt file not found!")


while True:
    print("\n===== PROJECT 02 =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you for using Project 02!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
