class ReplAlgo:
  def __init__(self, n_blocks, num_list, n_words, t_cache=1, t_mem=10, debug=False, nlt=True):
    self.n_blocks = n_blocks
    self.num_list = num_list
    self.age = [0 for i in range(n_blocks)]
    self.data = [None for i in range(n_blocks)]

    self.n_words = n_words
    self.t_cache = t_cache
    self.t_mem = t_mem
    
    self.avg_time = 0
    self.hits = 0
    self.misses = 0

    self.nlt = nlt
    self.debug = debug

  def is_full(self, data):
    for i in data:
      if i == None:
        return False
    return True

  def get_empty_space(self, data):
    ind = 0
    for i in data:
      if i == None:
        return ind
      ind += 1
    return -1

  def get_miss_penalty(self):
    if self.nlt:
      return self.t_cache + self.n_words * self.t_mem + self.t_cache
    else:
      return self.t_cache + self.t_mem 

  def get_total_time_lt(self):
    t_hits = self.hits * self.n_words * self.t_cache
    t_miss = self.misses * self.n_words * self.t_mem
    t_cache_probe_if_miss = self.misses * self.t_cache
    
    return t_hits + t_miss + t_cache_probe_if_miss

  def get_total_time_nlt(self):
    t_hits = self.hits * self.n_words * self.t_cache
    t_miss = self.misses * self.n_words * (self.t_mem + self.t_cache)
    t_cache_probe_if_miss = self.misses * self.t_cache
    
    return t_hits + t_miss + t_cache_probe_if_miss

  def get_hit_rate(self):
    return self.hits / (self.hits + self.misses)

  def get_avg_time(self):
    # hC + h'M
    return self.get_hit_rate() * self.t_cache + (1 - self.get_hit_rate()) * self.get_miss_penalty()

  def print_stats(self):
    print('----- Statistics -----')
    print('Total time (LT):\t\t', self.get_total_time_lt(), 'ns')
    print('Total time (NLT):\t\t', self.get_total_time_nlt(), 'ns')
    print('Average time:\t\t\t', self.get_avg_time(), 'ns')
    print('Hits:\t\t\t\t', self.hits)
    print('Misses:\t\t\t\t', self.misses)
    print('Hit Rate:\t\t\t', self.get_hit_rate() * 100, '%')
    print('Miss Rate:\t\t\t', (1 - self.get_hit_rate()) * 100, '%')
    print('Miss Penalty:\t\t\t', self.get_miss_penalty(), 'ns')

  def print_cache(self):
    pass

  def perform(self):
    pass  