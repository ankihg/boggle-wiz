# TO RUN
# `python3 -m unittest tests.board` from /boggle dir

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_board(self):
        board = Board()
        self.assertEqual(len(board.matrix), 4)
        for i in range(0, len(board.matrix)):
            self.assertEqual(len(board.matrix[i]), 4)

    def test_invalid_requirements_error(self):
        with self.assertRaises(ValueError):
            board = Board(4, 4, 12, 12)

if __name__ == '__main__':
    unittest.main()
