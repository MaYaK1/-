f = open('Sort.txt')
a1 = 0
I = 0



for line in f:
     a = line[0:-1]
     if len(a) == 8:
       if (a[0] == a[1] == a[2] == a[3] == a[4] == a[5] == a[6] == a[7]) :
         #print(a, len(a))
         a1 += 1
print ("Result", a1)
f.close;




