import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Player :

    def __init__(self):
        
        self.cards = []
        self.score = -1
        

    def pick_card(self):
        self.cards.append(random.choice(CARDS))
        self.score = self.calculate_score()

    def first_round(self):
        for i in range(2):
            self.cards.append(random.choice(CARDS))
        self.score = self.calculate_score()
        

    def stand(self):
        return True

    def calculate_score(self):
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0

        if 11 in self.cards and sum(self.cards) > 21:
            self.cards.remove(11)
            self.cards.append(1)

        return sum(self.cards)

        

