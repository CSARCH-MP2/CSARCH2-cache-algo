import random

for k in range(0, 10):
  with open(f'{k}.txt', 'w') as f:
    s = random.randint(1, 10)
    b = random.randint(1, 10)
    w = random.randint(2, 10)
    t_cache = random.randint(1, 20)
    t_mem = random.randint(21, 70)

    f.write(f't_cache: {t_cache}\n')
    f.write(f't_mem: {t_mem}\n')
    f.write(f'sets: {s}\n')
    f.write(f'n_blocks: {b}\n')
    f.write(f'words_per_block: {w}\n')

    for i in range(15):
      f.write(f'{random.randint(1, 8)}\n')

    f.close()