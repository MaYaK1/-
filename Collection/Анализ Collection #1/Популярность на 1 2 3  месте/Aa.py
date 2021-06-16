f = open('Sort.txt')
f1 = open('2.txt')
a1 = 0
a2 = 0
a3 = 0
I = 0


for c in f1:
  a1 = 0
  a2 = 0
  a3 = 0
  c1 = c[0:-1]
  print(c1)
  f = open('Sort.txt')
  for line in f:
     a = line[0:-1]
     a = a.lower()
     if ((len(c1)>0) and (len(a)>3)):
       if (c1[0] == a[0]) :
         a1 += 1
       if (c1[0] == a[1]) :
         a2 += 1
       if (c1[0] == a[2]) :
         a3 += 1  
  print ("Result", c1, a1 , a2 , a3)
  f.close;




