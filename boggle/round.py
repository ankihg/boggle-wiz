import copy
from trie import build_trie

class Round:

    def __init__(self, valid_words, board):
        self.trie_root = build_trie(valid_words)

        self.board = board
        self.board.generateMatrix()

        self.found_words = {}

    def solve(self):
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
    return (row_i, col_i) in used_positions

def _mark_position_as_used(used_positions, row_i, col_i):
    used_positions[(row_i, col_i)] = True
