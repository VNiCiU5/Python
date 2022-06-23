import numpy as np

array = np.empty(20, dtype=int)

for i in range(20):
    array[i] = input(i)

print(array)

for i in range(0,len(array)):
   if array[i] % 2 != 0:
       array[i] = 0
   elif array[i] < 30:
       array[i] = 1
   else:
       array[i] = 2

print(array)