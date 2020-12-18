from cache_alg.direct_mapping import DirectMapping
from cache_alg.lru_cache import LRU
from cache_alg.mru_cache import MRU
from cache_alg.bset_assoc import BlockSetAssociative

lines = open('./question7.txt', 'r').read().splitlines()
t_cache          = int(lines[0].split(' ')[1])
t_mem            = int(lines[1].split(' ')[1])
sets             = int(lines[2].split(' ')[1])
n_blocks_per_set = int(lines[3].split(' ')[1])
words_per_block  = int(lines[4].split(' ')[1])
num_list         = [int(i) for i in lines[5:]]
total_blocks     = n_blocks_per_set * sets

dm = DirectMapping(
  n_blocks=total_blocks, 
  num_list=num_list, 
  n_words=words_per_block, 
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('########################################################')
print('###############      Direct Mapping      ###############')
print('########################################################')
dm.perform()
dm.print_stats()


lru = LRU(
  n_blocks=total_blocks, 
  num_list=num_list, 
  n_words=words_per_block, 
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('\n')
print('########################################################')
print('###########      Full Associative - LRU      ###########')
print('########################################################')
lru.perform()
lru.print_stats()


mru = MRU(
  total_blocks, 
  num_list, 
  n_words=words_per_block, 
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('\n')
print('########################################################')
print('###########      Full Associative - MRU      ###########')
print('########################################################')
mru.perform()
mru.print_stats()


bs = BlockSetAssociative(
  n_sets=sets, 
  n_blocks=n_blocks_per_set, 
  num_list=num_list, 
  n_words=words_per_block,
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('\n')
print('########################################################')
print('###########         Block Set - LRU          ###########')
print('########################################################')
bs.lru()
bs.print_stats()


bs = BlockSetAssociative(
  n_sets=sets, 
  n_blocks=n_blocks_per_set, 
  num_list=num_list, 
  n_words=words_per_block,
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('\n')
print('########################################################')
print('###########         Block Set - MRU          ###########')
print('########################################################')
bs.mru()
bs.print_stats()