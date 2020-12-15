from mru_cache import MRU

lines = open('long.txt', 'r').read().splitlines()
n_blocks = int(lines[0])
num_list = [int(i) for i in lines[1:]]

mru = MRU(n_blocks, num_list, n_words=128, debug=True)
mru.perform()
mru.print_stats()