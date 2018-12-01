# TO RUN
# `python3 -m unittest tests.trie` from /boggle dir

import unittest
from main import TrieNode

class TestTrie(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
