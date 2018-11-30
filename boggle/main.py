import copy

class TrieNode:
    def __init__(self, char, is_word=False, children_by_char={}):
        self.char = char
        self.is_word = is_word
        self.children_by_char = children_by_char

    def has_next(self, char):
        return char in self.children_by_char

    def get_next(self, char):
        return self.children_by_char[char]


def build_trie(valid_words):
    trie_root = TrieNode('', False, {})
    for word in valid_words:
        build_trie_nodes(word, trie_root)
    return trie_root


def build_trie_nodes(word, trie_node):
    # c a r r o t
    for char in word:
        if char in trie_node.children_by_char:
            trie_node = trie_node.children_by_char[char]
        else:
            trie_node.children_by_char[char] = TrieNode(char, False, {})
            trie_node = trie_node.children_by_char[char]
    trie_node.is_word = True    # end of word, so mark as is_word


valid_words = [ 'carrot', 'cat', 'cats', 'car', 'cars', 'cell', 'bat', 'trap' ]
trie_root = build_trie(valid_words)
# True
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].is_word)
# False
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].children_by_char['r'].is_word)

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

board = Board()


class Round:

    def __init__(self, valid_words, board):
        self.trie_root = build_trie(valid_words)
        self.board = board
        self.found_words = {}

    def play(self):
        for row_i in range(0, self.board.num_rows):
            for col_i in range(0, self.board.num_cols):
                char = self.board.get_position(row_i, col_i)
                if self.trie_root.has_next(char):
                    self._visit_position(char, self.trie_root.get_next(char), row_i, col_i, {})
        return self.found_words

    # TODO exclude previosuly used positions
    def _visit_position(self, prefix, trie_node, row_i, col_i, used_positions):
        if trie_node.is_word:
            self.found_words[prefix] = True

        _mark_position_as_used(used_positions, row_i, col_i)
        for move in self.board.moves:
            next_row_i = move.get_row_i(row_i)
            next_col_i = move.get_col_i(col_i)
            if move.is_allowed(row_i, col_i) and trie_node.has_next(self.board.get_position(next_row_i, next_col_i)) and (not _is_position_used(used_positions, next_row_i, next_col_i)):
                next_char = self.board.get_position(next_row_i, next_col_i)
                self._visit_position(prefix + next_char, trie_node.get_next(next_char), next_row_i, next_col_i, copy.deepcopy(used_positions))

def _is_position_used(used_positions, row_i, col_i):
    return str(row_i) + ',' + str(col_i) in used_positions

def _mark_position_as_used(used_positions, row_i, col_i):
    used_positions[str(row_i) + ',' + str(col_i)] = True


round = Round(valid_words, board)
print(round.play())
