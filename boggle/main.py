from board import Board
from round import Round


board = Board()
round = Round(False, board)
print(round.board.matrix)
print(round.play())
