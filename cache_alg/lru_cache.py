from cache_alg.repl_algo import ReplAlgo

class LRU(ReplAlgo):
  '''
  Rules for LRU:
    1. if n in cache:
      update all younger ages by 1
      reset focused to 0
    else:
      2. if n not in cache and cache not full:
        update all ages by 1
        insert data to next dict
      3. if not in cache and cache full:
        find data with max age
        replace that age with 0
        update all ages by 1
        insert data in pos
  '''
  
  def print_cache(self):
    print('block\t|\tage\t|\tdata\t')
    print('--------------------------------------')
    for b in range(self.n_blocks):
      print(f'{b}\t|\t{self.age[b]}\t|\t{self.data[b]}')

    print('\n\n')

  def perform(self):
    for n in self.num_list:
      if n in self.data:
        if self.debug:
          print('Hit!')

        self.hits += 1
        ind = self.data.index(n)
        for a in range(len(self.data)):               # Update all younger blocks
          if self.age[a] < self.age[ind]:
            self.age[a] += 1

        self.age[ind] = 0

      else:
        if self.debug:
          print('Miss...')

        self.misses += 1
        if not self.is_full(self.data):
          emp = self.get_empty_space(self.data)
          for a in range(emp):                        # Update all previous ages
            self.age[a] += 1
          self.data[emp] = n                          # Put the value in the empty position
          self.age[emp] = 0                           # Set the age to 0
          
        else:
          ind_oldest = self.age.index(max(self.age))  # Get the position of the oldest cache 
          self.age[ind_oldest] = 0                    # Set the age of the oldest to 0
          for a in range(len(self.age)):              # Update all other ages by 1
            if a != ind_oldest:
              self.age[a] += 1
          self.data[ind_oldest] = n                   # Set the block of the lru cache to the incoming block

      if self.debug:
        print('n: ', n)
        self.print_cache()

    print('*************** Final ***************\n')
    self.print_cache()