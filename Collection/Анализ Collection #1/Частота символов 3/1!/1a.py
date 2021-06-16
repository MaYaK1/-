f1 = open('Combo3.txt')
f2 = open('Result Combo2.txt', 'w')
a1 = 0

from threading import Thread

def f():
    for c in f1:
      a1 = 0
      c1 = c[0:-1]
      f = open('Sort.txt' , 'r')
      for line in f:
         a = line[0:-1]
         if (c1 in a) :
           #print(a)
           a1 += 1
      print(str(c1) + str(' ') + str(a1))
      f2.write(str(c1) + str(' ') + str(a1) + '\n')
      f.close;

def f_2():
   for c in f1:
      a1 = 0
      c1 = c[0:-1]
      f = open('Sort.txt' , 'r')
      for line in f:
         a = line[0:-1]
         if (c1 in a) :
           #print(a)
           a1 += 1
      print(str(c1) + str(' ') + str(a1))
      f2.write(str(c1) + str(' ') + str(a1) + '\n')
      f.close; 


th_1, th_2= Thread(target=f), Thread(target = f_2)

if (__name__ == '__main__'):
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()
