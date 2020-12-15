from bset_assoc import BlockSetAssociative

n_sets = int(input())
n_blocks = int(input())
input_string = input()
num_list = [int(i) for i in input_string.split(' ')]

bs = BlockSetAssociative(n_sets, n_blocks, num_list, debug=False)
bs.mru()
