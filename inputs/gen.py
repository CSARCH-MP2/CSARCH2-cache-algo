with open('in.txt', 'w') as f: 
  f.write('16\n')
  f.write('4\n')
  for j in range(10):
    for i in range(68):
      f.write(f'{str(i)}\n')