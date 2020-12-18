with open('in.txt', 'w') as f: 
  f.write('sets: 8\nblocks_per_set: 4\nn_words: 128\n')
  f.write('0\n')
  for i in range(10):
    f.write('1\n')
    for j in range(20):
      f.write('2\n3\n')
    f.write('4\n5\n6\n7\n8\n9\n')
    
  f.write('10\n11\n')