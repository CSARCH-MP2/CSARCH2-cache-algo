from cache_alg.direct_mapping import DirectMapping
from cache_alg.lru_cache import LRU
from cache_alg.mru_cache import MRU
from cache_alg.bset_assoc import BlockSetAssociative

lines = open('./inputs/exercises/custom_time/6.txt', 'r').read().splitlines()
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

print('******************* Direct Mapping *******************')
dm.perform()
dm.print_stats()
print('\n-----------------------------------------------------\n')

lru = LRU(
  n_blocks=total_blocks, 
  num_list=num_list, 
  n_words=words_per_block, 
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('******************* Full Assoc LRU *******************')
lru.perform()
lru.print_stats()
print('\n-----------------------------------------------------\n')

mru = MRU(
  total_blocks, 
  num_list, 
  n_words=words_per_block, 
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('******************* Full Assoc MRU *******************')
mru.perform()
mru.print_stats()
print('\n-----------------------------------------------------\n')

bs = BlockSetAssociative(
  n_sets=sets, 
  n_blocks=n_blocks_per_set, 
  num_list=num_list, 
  n_words=words_per_block,
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('******************* Block Set LRU *******************')
bs.lru()
bs.print_stats()
print('\n-----------------------------------------------------\n')

bs = BlockSetAssociative(
  n_sets=sets, 
  n_blocks=n_blocks_per_set, 
  num_list=num_list, 
  n_words=words_per_block,
  t_cache=t_cache,
  t_mem=t_mem,
  debug=False)

print('******************* Block Set MRU *******************')
bs.mru()
bs.print_stats()
print('\n-----------------------------------------------------\n')