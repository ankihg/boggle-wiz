class TrieNode:
    def __init__(self, char, is_word=False, children_by_char={}):
        self.char = char
        self.is_word = is_word
        self.children_by_char = children_by_char


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


valid_words = [ 'carrot', 'cat', 'car', 'cars', 'cell', 'bat' ]
trie_root = build_trie(valid_words)
# True
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].is_word)
# False
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].children_by_char['r'].is_word)


class Board:
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    all_letters = vowels + consonants

    def __init__(self, num_rows=4, num_cols=4):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = self._generate()

    def _generate(self, min_vowels=4, min_consonants=4):
        # TODO
        return [
            [ 'c', 't', 'r', 's' ],
            [ 'b', 'a', 'r', 'i' ],
            [ 'b', 'o', 'f', 't' ],
            [ 't', 'a', 'r', 'e' ],
        ]

    def get_position(self, row_index, col_index):
        return self.matrix[row_index][col_index]

board = Board()
print(board.get_position(0, 3))
