import random

class Move:
    def __init__(self, is_allowed, get_row_i, get_col_i):
        self.is_allowed = is_allowed
        self.get_row_i = get_row_i
        self.get_col_i = get_col_i

class Board:
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    all_letters = vowels + consonants

    def __init__(self, num_rows=4, num_cols=4, min_vowels=4, min_consonants=4):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.min_vowels = min_vowels
        self.min_consonants = min_consonants

        if min_vowels + min_consonants > self.num_rows * self.num_cols:
            raise ValueError('`min_vowels` and `min_consonants` requirements are too large for board dimensions')

        self.matrix = self.generate()
        self.moves = [
            Move(lambda row_i, col_i: row_i > 0, lambda row_i: row_i - 1, lambda col_i: col_i), # up
            Move(lambda row_i, col_i: row_i < self.num_rows - 1, lambda row_i: row_i + 1, lambda col_i: col_i), # down
            Move(lambda row_i, col_i: col_i > 0, lambda row_i: row_i, lambda col_i: col_i - 1), # left
            Move(lambda row_i, col_i: col_i < self.num_cols - 1, lambda row_i: row_i, lambda col_i: col_i + 1), # right
            Move(lambda row_i, col_i: row_i > 0 and col_i > 0, lambda row_i: row_i - 1, lambda col_i: col_i - 1), # upleft
            Move(lambda row_i, col_i: row_i > 0 and col_i < self.num_cols - 1, lambda row_i: row_i - 1, lambda col_i: col_i + 1), # upright
            Move(lambda row_i, col_i: row_i < self.num_rows - 1 and col_i > 0, lambda row_i: row_i + 1, lambda col_i: col_i - 1), # downleft
            Move(lambda row_i, col_i: row_i < self.num_rows - 1 and col_i < self.num_cols - 1, lambda row_i: row_i + 1, lambda col_i: col_i + 1), # downright
        ]

    def generate(self):
        positions_to_populate = []
        matrix = []
        for row_i in range(0, self.num_rows):
            row = []
            matrix.append(row)
            for col_i in range(0, self.num_cols):
                row.append(None)
                positions_to_populate.append( (row_i, col_i) )

        for i in range(0, self.min_vowels):
            position = positions_to_populate.pop(random.randrange(len(positions_to_populate)))
            matrix[position[0]][position[1]] = Board.vowels[random.randrange(len(Board.vowels))]

        for i in range(0, self.min_vowels):
            position = positions_to_populate.pop(random.randrange(len(positions_to_populate)))
            matrix[position[0]][position[1]] = Board.consonants[random.randrange(len(Board.consonants))]

        while len(positions_to_populate) > 0:
            position = positions_to_populate.pop(random.randrange(len(positions_to_populate)))
            matrix[position[0]][position[1]] = Board.all_letters[random.randrange(len(Board.all_letters))]

        return matrix

    def get_position(self, row_index, col_index):
        return self.matrix[row_index][col_index]

    def print(self):
        for row_i in range(0, self.num_rows):
            print(self.matrix[row_i])
