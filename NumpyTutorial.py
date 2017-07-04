import numpy as np
import time
import sys

#list and numpy array size comparison
l = range(100)
print(sys.getsizeof(20)*len(l))

array = np.arange(100)
print(array.size*array.itemsize)

#computation time comparison

SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print("List took: ", (time.time()-start)*1000)
start = time.time()
res = a1 + a2
print("Numpy took: ", (time.time()-start)*1000)
