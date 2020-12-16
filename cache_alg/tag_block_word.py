import numpy as np

class TagBlockWord():
  '''
  n_blocks = number of blocks in cache
  n_words = number of words in block
  n_bits = number of bits in word
  n_way = number of blocks per set
  '''

  def __init__(self, n_cache_blocks, n_words_per_block, n_bits_per_word, n_mem_words, n_way=0, method='direct'):
    self.n_cache_blocks = n_cache_blocks
    self.n_words_per_block = n_words_per_block
    self.n_bits_per_word = n_bits_per_word
    self.n_mem_words = n_mem_words
    self.n_way = n_way
    self.method = method

  def get_mm_bits(self):
    return int(np.log2(self.n_mem_words))

  def get_tag(self):
    if self.method == 'bset':
      return self.get_mm_bits() - self.get_set() - self.get_word()
    elif self.method == 'fsa':
      return self.get_mm_bits() - self.get_word()
    else:
      return self.get_mm_bits() - self.get_block() - self.get_word()

  def get_block(self):
    if self.method == 'direct':
      return int(np.log2(self.n_cache_blocks))
    return 'No block - Not a direct-mapped cache'

  def get_word(self):
    return int(np.log2(self.n_words_per_block))

  def get_set(self):
    if self.method == 'bset':
      sets = self.n_cache_blocks // self.n_way
      return int(np.log2(sets))

    return 'No set - Not a block set-associative cache'

  def print_id(self):
    print('MM Bits', self.get_mm_bits())
    print('Tag: ', self.get_tag())
    print('Block: ', self.get_block())
    print('Set: ', self.get_set())
    print('Word: ', self.get_word())

