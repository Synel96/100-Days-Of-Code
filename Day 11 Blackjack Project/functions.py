import random

def new_card(player,computer, count = 1, choice = True, comp_choice = True):
    """Adds a specified number of cards to the player and/or the computer.

    Parameters:
    - player (list): The player's hand (list of integers).
    - computer (list): The computer's hand (list of integers).
    - count (int): Number of cards to add (default is 1).
    - choice (bool): If True, the player receives cards (default is True).
    - comp_choice (bool): If True, the computer receives cards (default is True)."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if choice :
        for i in range(count):
            player.append(random.choice(cards))
            
    if comp_choice :
        for i in range(count):
            computer.append(random.choice(cards))
            
    return player, computer

def sum_scores(player):
    """Calculates and returns the total score of the player's hand.

    Parameters:
    - player (list): The player's hand (list of integers).

    Returns:
    - int: The total score."""
    score = sum(player)
    return score
    

def computer_choice():
    """Simulates the computer's decision to draw a new card or not.

    Returns:
    - bool: True if the computer chooses to draw a card, False if it passes."""
    computer_pass =[True,False]
    return random.choice(computer_pass)



def check_winner(player1, player2,player_done,computer_done):
    """Checks if either player has exceeded 21 or if the game is over,
    and prints the result.

    Parameters:
    - player1 (int): The player's total score.
    - player2 (int): The computer's total score.
    - player_done (bool): True if the player has finished drawing cards.
    - computer_done (bool): True if the computer has finished drawing cards."""

    

    if player1 >= 21 and player2 >= 21 :
        print("Draw, both plyers went over 21! ")
    elif player1 >= 21:
        print("You went over you lose!")
    elif player2 >= 21 :
        print("Opponent went over! You Win!")


    if player_done == False and computer_done == False :
        if player1 == player2:
            print("Draw!")
        elif player1 > player2:
            print("You Win!")
        elif player1 < player2 :
            print("You Lose!")
