# Boggle Wiz
A program that generates and solves a game of boggle

- [Run](#run)
- [Test](#test)
- [Design](#design)


## Run
Run the following from the `./boggle` directory
```
python main.py
```

Output will resemble the following
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

- [Generate the board](#generate-board)
- [Build a trie of valid words](#build-trie)
- [Navigate the board](#navigate-board)

### Generate board

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
 (r)  [t]  (t)   
  |    |
 [r]  (s)
  |
 [o]
  |
 (t)
```

### Navigate board
