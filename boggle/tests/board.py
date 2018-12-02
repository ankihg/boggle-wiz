# TO RUN
# `python -m unittest tests.board` from /boggle dir

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_default_board(self):
        board = Board() # defaults to 4 x 4
        board.generate_matrix()
        self.assertEqual(len(board.matrix), 4)
        for i in range(0, len(board.matrix)):
            self.assertEqual(len(board.matrix[i]), 4)

    def test_custom_board(self):
        board = Board(6, 5) # has dimension 6 x 5
        board.generate_matrix()
        self.assertEqual(len(board.matrix), 6)
        for i in range(0, len(board.matrix)):
            self.assertEqual(len(board.matrix[i]), 5)

    def test_invalid_requirements_error(self):
        with self.assertRaises(ValueError):
            board = Board(4, 4, 12, 12)

if __name__ == '__main__':
    unittest.main()
