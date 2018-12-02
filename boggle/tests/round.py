# TO RUN
# `python -m unittest tests.round` from /boggle dir

import unittest
from round import Round
from board import Board

class TestRound(unittest.TestCase):

    def test_round(self):
        valid_words = [ 'carrot', 'cat', 'cats', 'car', 'cars', 'cell', 'komo' ]
        board = Board()
        board.matrix = [
            [ 'c', 't', 'r', 's' ],
            [ 'b', 'a', 'r', 'i' ],
            [ 'b', 'o', 'k', 'o' ],
            [ 't', 'a', 'r', 'm' ],
        ]
        round = Round(valid_words, board)
        found_words = round.solve()

        self.assertTrue('cat' in found_words)
        self.assertTrue('car' in found_words)
        self.assertTrue('cars' in found_words)
        self.assertTrue('carrot' in found_words)
        self.assertFalse('komo' in found_words) # uses already used positions
        self.assertFalse('ctrs' in found_words) # not a valid word



if __name__ == '__main__':
    unittest.main()
