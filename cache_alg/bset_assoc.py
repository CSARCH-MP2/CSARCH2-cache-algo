from cache_alg.repl_algo import ReplAlgo

'''
set 0
block | age | data
0       1       4  
1       0       5
2       3       6
3       2       8

set 1
block | age | data
0       1       4  
1       0       5
2       3       6
3       2       8

...

Input: 
num_sets
num_blocks/set
data_list

ex: 
4
1 2 3 4 5 4 3 1 2 5
'''

class BlockSetAssociative(ReplAlgo):

  def __init__(self, n_sets, n_blocks, num_list, n_words, t_cache, t_mem, debug=False):
    super(BlockSetAssociative, self).__init__(n_blocks, num_list, n_words, t_cache, t_mem, debug=debug)
    self.n_sets = n_sets
    self.cache = []
    for n in range(n_sets):
      self.cache.append({
        'age': [0 for i in range(self.n_blocks)],
        'data': [None for i in range(self.n_blocks)],
        'last_touch': [-1 for i in range(self.n_blocks)]
      })  

  def print_cache(self, algo='lru'):
    print('************************************************')
    for set_num in range(self.n_sets):
      print('Set:', set_num)
      if algo == 'lru':
        print('block\t|\tage\t|\tdata\t')
      elif algo == 'mru':
        print('block\t|\tdata\t')

      print('--------------------------------------')
      for b in range(self.n_blocks):
        if algo == 'lru':
          print(f'{b}\t|\t{self.cache[set_num]["age"][b]}\t|\t{self.cache[set_num]["data"][b]}')
        elif algo == 'mru':
          print(f'{b}\t|\t{self.cache[set_num]["data"][b]}')
      print('\n')
    print('************************************************')
    print('\n')
    
  def lru(self):
    for n in self.num_list:
      set_num = n % self.n_sets

      if n in self.cache[set_num]['data']:
        if self.debug:
          print('Hit!')
        self.hits += 1  
        ind = self.cache[set_num]['data'].index(n)
        for a in range(len(self.cache[set_num]['data'])):
          if self.cache[set_num]['age'][a] < self.cache[set_num]['age'][ind]:
            self.cache[set_num]['age'][a] += 1

        self.cache[set_num]['age'][ind] = 0

      else:
        if self.debug:
          print('Miss...')

        self.misses += 1
        if not self.is_full(self.cache[set_num]['data']):
          emp = self.get_empty_space(self.cache[set_num]['data'])
          for a in range(emp):
            self.cache[set_num]['age'][a] += 1
          self.cache[set_num]['data'][emp] = n
          self.cache[set_num]['age'][emp] = 0
          
        else:
          ind_oldest = self.cache[set_num]['age'].index(max(self.cache[set_num]['age']))
          self.cache[set_num]['age'][ind_oldest] = 0
          for a in range(len(self.cache[set_num]['age'])):
            if a != ind_oldest:
              self.cache[set_num]['age'][a] += 1
          self.cache[set_num]['data'][ind_oldest] = n

      if self.debug:
        print('n: ', n)
        self.print_cache()

    print('*************** Final ***************\n')
    self.print_cache()

  def mru(self):
    for n in self.num_list:
      set_num = n % self.n_sets
      if n in self.cache[set_num]['data']:
        if self.debug:
          print('Hit!')

        self.hits += 1
        self.cache[set_num]['last_touch'] = self.cache[set_num]['data'].index(n)

      else:
        if self.debug:
          print('Miss...')

        self.misses += 1
        if not self.is_full(self.cache[set_num]['data']):
          emp = self.get_empty_space(self.cache[set_num]['data'])
          self.cache[set_num]['data'][emp] = n
          self.cache[set_num]['last_touch'] = emp
          
        else:
          lt = self.cache[set_num]['last_touch']
          self.cache[set_num]['data'][lt] = n

      if self.debug:
        print('n: ', n)
        self.print_cache('mru')

    print('*************** Final ***************\n')
    self.print_cache('mru')
