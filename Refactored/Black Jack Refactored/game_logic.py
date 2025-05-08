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
        print(self.compare())

    def ask_player(self):
        input("Type 'y' to get another card, type 'n' to pass: ")


    def compare(self):
        """Compares the user score against the computer score."""

        if self.player.score == self.computer.score:
            return "Draw 🙃"
        elif self.computer.score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif self.player.score == 0:
            return "Win with a Blackjack 😎"
        elif self.player.score > 21:
            return "You went over. You lose 😭"
        elif self.computer.score > 21:
            return "Opponent went over. You win 😁"
        elif self.player.score > self.computer.score:
            return "You win 😃"
        else:
            return "You lose 😤"
        
