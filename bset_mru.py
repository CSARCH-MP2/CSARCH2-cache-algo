from cache_alg.bset_assoc import BlockSetAssociative

lines = open('./inputs/bset_input.txt', 'r').read().splitlines()
n_sets = int(lines[0].split(' ')[1])
n_blocks_per_set = int(lines[1].split(' ')[1])
n_words_per_block = int(lines[2].split(' ')[1])
print(n_sets, n_blocks_per_set, n_words_per_block)

num_list = [int(i) for i in lines[3:]]

bs = BlockSetAssociative(
  n_sets, 
  n_blocks_per_set, 
  num_list, 
  n_words=n_words_per_block,
  debug=False)

bs.mru()
bs.print_stats()