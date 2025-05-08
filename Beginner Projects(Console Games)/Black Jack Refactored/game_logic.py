class Game_Logic:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def display_status(self):
        print(f"Your cards: {self.player.cards}, current score: {self.player.score}")
        print(f"Computer's first card: {self.computer.cards[0]}")

    
    def end_status(self):
        print(f"Your final hand: {self.player.cards}, final score: {self.player.score}")
        print(f"Computer's final hand: {self.computer.cards}, final score: {self.computer.score}")


    def ask_player(self):
        input("Type 'y' to get another card, type 'n' to pass: ")

        
