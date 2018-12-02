# TO RUN
# `python3 -m unittest tests.board` from /boggle dir

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    # def test_board(self):
    #

    def test_invalid_requirements_error(self):
        with self.assertRaises(ValueError):
            board = Board(4, 4, 12, 12)

if __name__ == '__main__':
    unittest.main()
