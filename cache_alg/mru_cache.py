from repl_algo import ReplAlgo


class MRU(ReplAlgo):
  def print_cache(self):
    print('block\t|\tdata\t')
    print('---------------------')
    for b in range(self.n_blocks):
      print(f'{b}\t|\t{self.data[b]}')
    print('\n\n')

  def perform(self):
    last_touch = 0
    for n in self.num_list:
      if n in self.data:
        if self.debug:
          print('Hit!')

        self.hits += 1
        last_touch = self.data.index(n)

      else:
        if self.debug:
          print('Miss...')

        self.misses += 1
        if not self.is_full(self.data):
          emp = self.get_empty_space(self.data)
          self.data[emp] = n
          last_touch = emp
          
        else:
          self.data[last_touch] = n

      if self.debug:
        print('n: ', n)
        self.print_cache()

    print('*************** Final ***************\n')
    self.print_cache()