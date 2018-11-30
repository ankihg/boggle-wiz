# Design

## Build trie from valid words


## Generate board


## Navigate board while depth first traversing trie

###### Mark already used positions
- Keep hash of used index pairs

###### Collect valid words
- In hash to prevent duplicates

###### Navigate

- Double loop thru matrix
- At each position
    - Check all directions (excluding previously used positions)
    - For each direction
        - If next character on trie for prefix
            - Recurse to next position, passing string in progress
            - If that character on trie creates valid word
                - Add to collected words


# Questions

## If same word can be generate thru multiple paths, do you count it twice?
Gonna say no

## Will valid word list only contain words 3 char or longer?
