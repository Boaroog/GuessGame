import random

fruits = ["BANANA", "GRAPE", "DATES", "BERRY", "APPLE", "MANGO"]
Tries = 5
fav_fruits_length = 3


def generate_fav_fruits():
    fav_fruits = []

    for _ in range(fav_fruits_length):
        fruit = random.choice(fruits)
        fav_fruits.append(fruit)

    return fav_fruits


def guess_fav_fruits():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != fav_fruits_length:
            print(f"You must guess {fav_fruits_length} fruits.")
            continue

        for fruit in guess:
            if fruit not in fruits:
                print(f"Invalid fruit: {fruit}. Try your luck again.")
                break
        else:
            break

    return guess


def check_fav_fruits(guess, real_fav_fruits):
    fruit_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for fruit in real_fav_fruits:
        if fruit not in fruit_counts:
            fruit_counts[fruit] = 0
        fruit_counts[fruit] += 1

    for guess_fruit, real_fruit in zip(guess, real_fav_fruits):
        if guess_fruit == real_fruit:
            correct_pos += 1
            fruit_counts[guess_fruit] -= 1

    for guess_fruit, real_fruit in zip(guess, real_fav_fruits):
        if guess_fruit in fruit_counts and fruit_counts[guess_fruit] > 0:
            incorrect_pos += 1
            fruit_counts[guess_fruit] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to my Favourite Fruits Guess Game, you have {Tries} attempts to guess the right fruits....")
    print("The valid favourite fruits are:", *fruits)

    fav_fruits = generate_fav_fruits()
    for attempts in range(1, Tries + 1):
        guess = guess_fav_fruits()
        correct_pos, incorrect_pos = check_fav_fruits(guess, fav_fruits)

        if correct_pos == fav_fruits_length:
            print(f"You guessed my favourite fruits in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries, the code, the code was: ", *fav_fruits)


if __name__ == "__main__":
    game()
