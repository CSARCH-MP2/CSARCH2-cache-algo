'''
Mapping Algorithms (Block Set Associative)
Input: 
  Number of blocks in the cache
  Array of numbers to insert to "cache", delimited by a space
  
  ex: 
  4
  1 2 3 4 3 1 5

Output: Table showing the block number, age, and data at a given block
  ex: 
    block   |   age   | data
    ------------------------
    0           1         2
    1           0         0
    2           2         5
    3           3         6
'''

from bset_assoc import BlockSetAssociative

n_sets = int(input())
n_blocks = int(input())
input_string = input()
num_list = [int(i) for i in input_string.split(' ')]

bs = BlockSetAssociative(n_sets, n_blocks, num_list, debug=True)
bs.mru()