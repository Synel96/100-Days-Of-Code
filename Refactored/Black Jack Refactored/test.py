import unittest


from player import Player

class TestPlayer(unittest.TestCase):

    def test_first_round_adds_two_cards(self):
        player = Player()
        player.first_round()
        self.assertEqual(len(player.cards), 2)

    def test_score_after_first_round_is_valid(self):
        player = Player()
        player.first_round()
        self.assertIsInstance(player.score, int)
        self.assertGreater(player.score, 0)

    def test_blackjack_is_zero_score(self):
        player = Player()
        player.cards = [10, 11]  
        score = player.calculate_score()
        self.assertEqual(score, 0)


    def test_ace_adjustment(self):
        player = Player()
        player.cards = [11, 9, 5]  
        score = player.calculate_score()
        self.assertEqual(score, 15)

    def test_stand(self):
        player = Player()
        
        player.stand()
        self.assertEqual(player.wants_to_play,False)






if __name__ == '__main__':
    unittest.main()