from cache_alg.direct_mapping import DirectMapping

lines = open('./inputs/dm_input.txt', 'r').read().splitlines()
n_blocks = int(lines[0])
num_list = [int(i) for i in lines[1:]]

dm = DirectMapping(n_blocks, num_list, n_words=2, debug=False)
dm.perform()
dm.print_stats()