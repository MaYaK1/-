import itertools


print(*map(''.join, itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#%^&*()+-;:?{}[]{,.}$', repeat=2)))
