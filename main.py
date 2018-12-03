import time
from board import Board
from round import Round

def run(num_rows, num_cols, min_vowels, min_consonants):
    print('> INITIALIZING THE BOARD ...')
    board = Board(num_rows, num_cols, min_vowels, min_consonants)
    print('> BUILDING VALID WORDS TRIE ...')
    round = Round(board)

    print('\n')
    print('> HERE IS THE BOARD')
    round.board.print()
    print('\n')

    start_time = time.time()
    found_words_dict = round.solve()
    end_time = time.time()
    time_elapsed = end_time - start_time

    found_words = list(found_words_dict.keys())
    print('>', len(found_words), 'WORDS FOUND IN', time_elapsed, 'SECONDS')
    print(found_words)
