import art
import random
import functions

player_cards = []
computer_cards = []
player_score = 0
computer_score = 0
player_choice = True
computer_choice = True


# welcome
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if choice == "y" :
  #First Round
    print(art.logo)
    functions.new_card(player_cards,computer_cards,2)

    print(f"Your Cards : {player_cards}, Your Score :{functions.sum_scores(player_cards)}")
    print(f"Computer first card : {computer_cards[0]} ")
    
    #Both the computer and the player choose whether to pass or continue playing.

    choice2 = input("Type 'y' to get another card, type 'n' to pass:").lower()
    computer_choice = functions.computer_choice()
    print(computer_choice)

    #The dealing begins, followed by the second round.
    if choice == "y" and computer_choice :
         
         player_cards, computer_cards = functions.new_card(player_cards, computer_cards,1, True, True,)
         player_score = functions.sum_scores(player_cards)
         computer_score = functions.sum_scores(computer_cards)
         functions.check_winner(player_score,computer_score,True,True)
    
    elif choice == "n" and computer_choice:
         player_cards, computer_cards = functions.new_card(player_cards, computer_cards,1, False, True,)
         computer_score = functions.sum_scores(computer_cards)
         functions.check_winner(player_score,computer_score,False,True)

    print(f"Your Cards : {player_cards}, Your Score :{functions.sum_scores(player_cards)}")
    print(f"Computer first card : {computer_cards[0]} ")
    print(player_cards)
    print(computer_cards)










    




