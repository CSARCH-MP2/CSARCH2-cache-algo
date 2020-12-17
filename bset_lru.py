from cache_alg.bset_assoc import BlockSetAssociative

lines = open('./inputs/exercises/custom_time/0.txt', 'r').read().splitlines()
t_cache          = int(lines[0].split(' ')[1])
t_mem            = int(lines[1].split(' ')[1])
sets             = int(lines[2].split(' ')[1])
n_blocks_per_set = int(lines[3].split(' ')[1])
words_per_block  = int(lines[4].split(' ')[1])
num_list         = [int(i) for i in lines[5:]]

bs = BlockSetAssociative(
  n_sets=sets, 
  n_blocks=n_blocks_per_set, 
  num_list=num_list, 
  n_words=words_per_block,
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

bs.lru()
bs.print_stats()