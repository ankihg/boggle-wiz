class Move:
    def __init__(self, is_allowed, get_row_i, get_col_i):
        self.is_allowed = is_allowed
        self.get_row_i = get_row_i
        self.get_col_i = get_col_i

class Board:
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    all_letters = vowels + consonants

    def __init__(self, num_rows=4, num_cols=4):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = self._generate()
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

    def _generate(self, min_vowels=4, min_consonants=4):
        # TODO
        # return [
        #     [ 's', 't', 'c', 's' ],
        #     [ 't', 'r', 'a', 'p' ],
        #     [ 'a', 'o', 'r', 't' ],
        #     [ 'c', 'a', 's', 'e' ],
        # ]
        return [
            [ 'c', 't', 'r', 's' ],
            [ 'b', 'a', 'r', 'i' ],
            [ 'b', 'o', 'f', 't' ],
            [ 't', 'a', 'r', 'e' ],
        ]

    def get_position(self, row_index, col_index):
        return self.matrix[row_index][col_index]
