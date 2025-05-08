
from player import Player 
from computer import Computer
from game_logic import Game_Logic
from art import logo


computer = Computer()
player = Player()
logic = Game_Logic(player,computer)

def play_game():

    is_game_over = False

    player.first_round()
    computer.first_round()

    while not is_game_over:

        logic.display_status()

        if player.score == 0 or computer.score == 0 or player.score > 21:
            is_game_over = True
        else:
            should_deal = logic.ask_player()
            if should_deal == "y":
                player.pick_card()
            else:
                is_game_over = True




print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
          







