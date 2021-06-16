f = open('Sort.txt')
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0


for line in f:
  if (len(line) == 81) :
        print(line)
        a1 += 1
  if (len(line) == 83) :
        a2 += 1
  if (len(line) == 84) :
        a3 += 1
  if (len(line) == 85) :
        a4 += 1
  if (len(line) == 86) :
        a5 += 1
  if (len(line) == 87) :
        a6 += 1
  if (len(line) == 88) :
        a7 += 1
  if (len(line) == 89) :
        a8 += 1
  if (len(line) == 90) :
        a9 += 1
  if (len(line) == 91) :
        a10 += 1
print(a1, "81 символ")
print(a2, "82 символ")
print(a3, "83 символ")
print(a4, "84 символ")
print(a5, "85 символ")
print(a6, "86 символ")
print(a7, "87 символ")
print(a8, "88 символ")
print(a9, "89 символ")
print(a10, "90 символ")



