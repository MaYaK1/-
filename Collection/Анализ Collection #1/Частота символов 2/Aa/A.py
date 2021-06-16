f1 = open('Combo2.txt')
f2 = open('Result Combo2.txt', 'w')
a1 = 0

for c in f1:
  a1 = 0
  c1 = c[0:-1]
  f = open('Sort.txt' , 'r')
  for line in f:
     a = line[0:-1]
     #a = a.lower()
     if (c1 in a) :
       a1 += 1
  print(str(c1) + str(' ') + str(a1))
  f2.write(str(c1) + str(' ') + str(a1) + '\n')
  f.close;

