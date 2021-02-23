from random import randint
from time import sleep


# User guess input
def get_user_guess():
    guess = int(input("Guess the number: "))
    return guess


# Roll dice
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print(f"The number is between 1 and {max_val}.")
    guess = get_user_guess()
    if guess > max_val or guess < 1:
        print(f"Error. Please enter a number between 1 and {max_val}.")
    else:
        print("Rolling...")
        sleep(2)
        print(f"First roll: {first_roll}")
        sleep(1)
        print(f"Second roll: {second_roll}")
        sleep(1)
        total_roll = first_roll + second_roll
        print("Result...")
        sleep(2)
        print(f"Rolled: {total_roll}")
        if guess == total_roll:
            print("We have a winner!")
        else:
            print("You lost. Try another time.")
