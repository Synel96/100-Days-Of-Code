from player import Player 
from computer import Computer
from game_logic import Game_Logic
from art import logo

def play_game():

    computer = Computer()
    player = Player()
    logic = Game_Logic(player,computer)

    is_game_over = False

    print(logo)
    player.first_round()
    computer.first_round()

    while not is_game_over :

        logic.display_status()

        if player.score == 0 or computer.score == 0 or player.score > 21:
                is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player.pick_card()
            else:
                is_game_over = True


    while computer.score != 0 and computer.score < 17:
            computer.pick_card()
            
    logic.end_status()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

   



   

   







