from lru_cache import LRU

lines = open('long.txt', 'r').read().splitlines()
n_blocks = int(lines[0])
num_list = [int(i) for i in lines[1:]]

lru = LRU(n_blocks, num_list, n_words=128, debug=True)
lru.perform()
lru.print_stats()