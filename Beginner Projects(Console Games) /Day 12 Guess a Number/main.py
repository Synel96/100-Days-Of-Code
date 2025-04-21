import random
import art

number_to_guess = random.randint(1,100)
difficulty =""
number_of_guess = 10
game_over = False

def guess_the_number():

    number_to_guess = random.randint(1,100)
    difficulty =""
    number_of_guess = 10
    game_over = False
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "hard":
        number_of_guess = 5
    while not game_over:
        if number_of_guess == 0 :
            print(f"You've run out of guesses! The guessed number was {number_to_guess}!" )
            game_over = True
            new_game = input("Would you like to try again? Answer with 'y' or 'n' :").lower()
            if new_game == "y":
                print("\n" * 20)
                guess_the_number()

        guessed_number = int(input("Make a guess: "))
        if guessed_number < number_to_guess :
            print("Too low.")
            print("Guess again.")
            number_of_guess -= 1
            print(f"You have {number_of_guess} attempts remaining to guess the number!")
        elif guessed_number > number_to_guess :
            print("Too high.")
            print("Guess again.")
            number_of_guess -= 1
            print(f"You have {number_of_guess} attempts remaining to guess the number!")
        elif guessed_number == number_to_guess:
            print(f"You got it the answer was {number_to_guess}!")
            game_over = True
            new_game = input("Would you like to try again? Answer with 'y' or 'n' :")
            if new_game == "y":
                print("\n" * 20)
                guess_the_number()

guess_the_number()