# Boggle Wiz
A program that generates and solves a game of boggle

- [Run](#run)
- [Test](#test)
- [Design](#design)


## Run
Run the following from the `./boggle` directory to run with default parameters
```
python play.py
```

For a custom play, the program takes the following optional arguments
```
--num_rows NUM_ROWS  number of rows on board
--num_cols NUM_COLS  number of columns on board
--min_vow MIN_VOW    minimum number of vowels on board
--min_cons MIN_CONS  minimum number of consonants on board
```

Play output will resemble the following
```
> INITIALIZING THE BOARD ...
> BUILDING VALID WORDS TRIE ...


> HERE IS THE BOARD
['d', 'm', 'i', 'b']
['r', 'a', 'e', 'e']
['v', 'm', 'c', 'b']
['h', 't', 'c', 'a']


> 104 WORDS FOUND IN 0.014575958251953125 SECONDS
['dram', 'drame', 'dam', 'damie', 'dame', 'dar', 'dae', 'dace', 'mam', 'mar', 'marm', 'mae', 'mad', 'mac', 'mace', 'mib', 'mia', 'miae', 'mecca', 'mea', 'mear', 'mead', 'mee', 'mem', 'ima', 'imam', 'bee', 'bec', 'became', 'becard', 'bim', 'bima', 'bea', 'beam', 'bear', 'beard', 'bearm', 'bead', 'bema', 'bemar', 'bemad', 'bemaim', 'ram', 'rami', 'ramie', 'rame', 'ramee', 'rad', 'race', 'ami', 'amie', 'ame', 'ameba', 'amt', 'arm', 'adm', 'admi', 'aim', 'aimee', 'ace', 'acc', 'acct', 'acca', 'acme', 'act', 'ecca', 'ecb', 'ecad', 'eam', 'ear', 'ead', 'emda', 'var', 'vai', 'vac', 'mamie', 'maim', 'cee', 'ccm', 'cam', 'came', 'car', 'card', 'cad', 'cai', 'cav', 'cab', 'bac', 'bacca', 'baccar', 'baccae', 'bact', 'tmema', 'tmh', 'cace', 'cacei', 'caca', 'cacam', 'abe', 'abc', 'abeam', 'abear', 'acce', 'acad']
```

## Test
Run the following from the `./boggle` directory
```
python -m unittest tests.board tests.round tests.trie
```

## Design
The task is broken into the following three sections

- [Build a trie of valid words](#build-trie)
- [Generate the board](#generate-board)
- [Navigate the board](#navigate-board)

### Build trie
A trie is an ideal data structure for the scenario because you can traverse the trie as you are navigating through the board.

The program reads the `valid-words` file line by line, adding each word to the trie. On the last character of each word, the node is marked as `is_word`, so during the navigation process any node that `is_word` can be added to the collection of found words.


The following is a sample trie fed only the words `['car', 'carrot', 'cats', 'bat']`. Nodes surrounded by `( )` denotes `is_word` and `[ ]` not `is_word`.
```
      ['']
    /      \
   [c]      [b]
    |        |
   [a]      [a]
   /  \      |
 (r)  [t]   (t)   
  |    |
 [r]  (s)
  |
 [o]
  |
 (t)
```

With more time I would write the trie out to file once it is built, so it can just be read in, instead of regenerated, on subsequent rounds.

### Generate board
To generate the board, the program creates a list of all positions to populate. It then randomly selects positions from the list, first choosing random vowels until the minimum vowel requirement is met, and then does the same with consonants, placing each letter on the board as it is chosen. With the remaining positions to populate, it randomly selects from a list of all letters.

### Navigate board
At each position, a list of potential next moves is evaluated.

If the move is allowed (i.e. it won't take you off the edge of the board), the resulting position has not already been used in the progressing word, and the resulting character is a next character for the current node of the trie, then the program recurses into the next position, passing the next node of the trie and a deep copy of the `used_positions` dictionary.

At each point of recursion, if the current trie node is marked as `is_word`, then the current string is added to the `found_words` dictionary.
