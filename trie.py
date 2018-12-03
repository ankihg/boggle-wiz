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
    if valid_words:
        for word in valid_words:
            build_trie_nodes(word, trie_root)
    else:
        with open('./resources/valid-words.txt', 'r') as lines:
            for word in lines:
                trimmed_word = word.strip()
                if len(trimmed_word) >= 3:
                    build_trie_nodes(trimmed_word.lower(), trie_root)
    return trie_root

def build_trie_nodes(word, trie_node):
    # c a r r o t
    for char in word:
        # print('c', char)
        if char in trie_node.children_by_char:
            trie_node = trie_node.children_by_char[char]
        else:
            trie_node.children_by_char[char] = TrieNode(char, False, {})
            trie_node = trie_node.children_by_char[char]
    trie_node.is_word = True    # end of word, so mark as is_word
