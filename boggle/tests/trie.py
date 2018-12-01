# TO RUN
# `python3 -m unittest tests.trie` from /boggle dir

import unittest
from trie import build_trie

class TestTrie(unittest.TestCase):

    def test_trie(self):
        valid_words = [ 'carrot', 'cat', 'cats', 'car', 'cars', 'cell', 'bat' ]
        trie_root = build_trie(valid_words)

        # car is a valid word
        self.assertTrue(trie_root.get_next('c').get_next('a').get_next('r').is_word)
        # carr is not a valid word
        self.assertFalse(trie_root.get_next('c').get_next('a').get_next('r').get_next('r').is_word)
        # cat is a valid word
        self.assertTrue(trie_root.get_next('c').get_next('a').get_next('t').is_word)

        # no valid words start with x
        self.assertFalse(trie_root.has_next('x'))



if __name__ == '__main__':
    unittest.main()
