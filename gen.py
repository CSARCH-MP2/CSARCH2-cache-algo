import random

with open(f'question7.txt', 'w') as f:
  f.write(f't_cache: 1\n')
  f.write(f't_mem: 10\n')
  f.write(f'sets: 8\n')
  f.write(f'n_blocks_per_set: 2\n')
  f.write(f'words_per_block: 16\n')

  for j in range(20):
    f.write(f'{j}\n')

  f.close()