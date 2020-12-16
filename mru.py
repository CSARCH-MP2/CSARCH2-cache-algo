from cache_alg.mru_cache import MRU

lines = open('./inputs/fa_input.txt', 'r').read().splitlines()
n_blocks = int(lines[0].split(' ')[1])
words_per_block = int(lines[1].split(' ')[1])
num_list = [int(i) for i in lines[2:]]

mru = MRU(n_blocks, num_list, n_words=words_per_block, debug=False)
mru.perform()
mru.print_stats()