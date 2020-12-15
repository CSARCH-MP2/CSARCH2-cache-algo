class ReplAlgo:
  def __init__(self, n_blocks, num_list, debug=False):
    self.n_blocks = n_blocks
    self.num_list = num_list
    self.age = [0 for i in range(n_blocks)]
    self.data = [None for i in range(n_blocks)]
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

  def print_cache(self):
    pass

  def perform(self):
    pass  