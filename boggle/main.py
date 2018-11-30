class TrieNode:
    def __init__(self, char, is_word, children_by_char):
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
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].is_word)
print(trie_root.children_by_char['c'].children_by_char['a'].children_by_char['r'].children_by_char['r'].is_word)
