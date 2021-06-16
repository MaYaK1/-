f = open('Sort.txt')
f1 = open('2.txt')
a1 = 0
I = 0

ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for c in f1:
  a1 = 0
  c1 = c[0:-1]
  print(c1)
  f = open('Sort.txt')
  for line in f:
     a = line[0:-1]
     a = a.lower()
     if (c1 in a) :
       a1 += 1
  print ("Result", a1)
  f.close;




