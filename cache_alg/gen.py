with open('long.txt', 'w') as f: 
  f.write('8\n0\n')
  for i in range(10):
    f.write('1\n')
    for i in range(20):
      f.write('2\n3\n')
    f.write('4\n5\n6\n7\n8\n9\n')
  
  f.write('10\n11\n')