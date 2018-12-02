import time
from board import Board
from round import Round

print('INITIALIZING THE BOARD ...')
board = Board()
print('BUILDING VALID WORDS TRIE ...')
round = Round(False, board)

print('\n')
print('BOARD')
round.board.print()
print('\n')

start_time = time.time()
found_words_dict = round.solve()
end_time = time.time()
time_elapsed = end_time - start_time

found_words = list(found_words_dict.keys())
print(len(found_words), 'WORDS FOUND IN', time_elapsed, 'SECONDS')
print(found_words)
