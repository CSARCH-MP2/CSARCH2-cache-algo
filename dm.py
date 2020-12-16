from cache_alg.direct_mapping import DirectMapping

lines = open('./inputs/dm_input.txt', 'r').read().splitlines()
n_blocks = int(lines[0].split(' ')[1])
words_per_block = int(lines[1].split(' ')[1])
num_list = [int(i) for i in lines[2:]]

dm = DirectMapping(n_blocks, num_list, n_words=words_per_block, debug=False)
dm.perform()
dm.print_stats()