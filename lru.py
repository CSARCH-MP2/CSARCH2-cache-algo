from cache_alg.lru_cache import LRU

lines = open('./inputs/fa_input.txt', 'r').read().splitlines()
n_blocks = int(lines[0].split(' ')[1])
words_per_block = int(lines[1].split(' ')[1])
num_list = [int(i) for i in lines[2:]]

lru = LRU(n_blocks, num_list, n_words=words_per_block, debug=False)
lru.perform()
lru.print_stats()