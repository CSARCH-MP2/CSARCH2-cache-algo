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
    stats = ""
    stats += '----- Statistics -----\n'
    print('----- Statistics -----')
    print('Total time (LT):\t\t', self.get_total_time_lt(), 'ns')
    stats = stats + 'Total time (LT):\t\t' + str(self.get_total_time_lt()) + 'ns\n'
    print('Total time (NLT):\t\t', self.get_total_time_nlt(), 'ns')
    stats = stats + 'Total time (NLT):\t\t'+str(self.get_total_time_nlt())+ 'ns\n'
    print('Average time:\t\t\t', self.get_avg_time(), 'ns')
    stats =  stats + 'Average time:\t\t\t' + str(self.get_avg_time()) + 'ns\n'
    print('Hits:\t\t\t\t', self.hits)
    stats =  stats + 'Hits:\t\t\t\t' + str(self.hits) +'\n'
    print('Misses:\t\t\t\t', self.misses)
    stats =  stats + 'Misses:\t\t\t\t' + str(self.misses) + '\n'
    print('Hit Rate:\t\t\t', self.get_hit_rate() * 100, '%')
    stats = stats + 'Hit Rate:\t\t\t'+ str(self.get_hit_rate() * 100) +'%\n'
    print('Miss Rate:\t\t\t', (1 - self.get_hit_rate()) * 100, '%')
    stats = stats + 'Miss Rate:\t\t\t'+ str((1 - self.get_hit_rate()) * 100) +'%\n'
    print('Miss Penalty:\t\t\t', self.get_miss_penalty(), 'ns')
    stats = stats + 'Miss Penalty:\t\t\t' + str(self.get_miss_penalty()) + 'ns\n'
    return stats

  def print_cache(self):
    pass

  def perform(self):
    pass  