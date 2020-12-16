from cache_alg.repl_algo import ReplAlgo

class DirectMapping(ReplAlgo):
  def print_cache(self):
    print('block\t|\tdata\t')
    print('---------------------')
    for b in range(self.n_blocks):
      print(f'{b}\t|\t{self.data[b]}')
    print('\n\n')

  def perform(self):
    for n in self.num_list:
      if self.debug:
        print('n: ', n)

      if n in self.data:
        self.hits += 1
      else: 
        self.misses += 1

      self.data[n % self.n_blocks] = n
      if self.debug:
        self.print_cache()

    print('*************** Final ***************\n')
    self.print_cache()