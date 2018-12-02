from board import Board
from round import Round


board = Board()
round = Round(False, board)
print('BOARD')
round.board.print()
print(round.play())
