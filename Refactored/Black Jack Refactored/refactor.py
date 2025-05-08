
from player import Player 
from computer import Computer
from game_logic import Game_Logic
from art import logo






computer = Computer()
player = Player()
logic = Game_Logic(player,computer)



player.first_round()
computer.first_round()


   







