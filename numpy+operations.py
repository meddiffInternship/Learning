
# coding: utf-8

# In[3]:

import numpy as np


# In[9]:

#creating array
a = np.array([10,12,1993])
a[2]


# # nump array vs  python list

# In[10]:

import time
import sys


# In[13]:

#less memory allocation
l = range(100)
print(sys.getsizeof(5)*len(l))

ar = np.arange(100)
print(ar.size*ar.itemsize)


# In[18]:

#fast and convenient
SIZE = 100000
a1 = range(SIZE)
a2 = range(SIZE)
n1 = np.arange(SIZE)
n2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(a1,a2)]
print("python list took",(time.time()-start)*1000)
#time taken by 
start = time.time()
result = n1+n2
print("numpy array took",(time.time()-start)*1000)


# In[24]:

#convenient method
c1 = np.array([5,4,3])
c2 = np.array([8,7,9])
print(c1+c2)
print(c2-c1)
print(c2*c1)
print(c2/c1)


# # creating n-dimensional array

# In[49]:

#creating 1 dimensional array
m = np.array([1,2,3])
print(m)
#creating n dimensional array
m1 = np.array([[1,2],[4,5],[8,6]])
print(m1)
#to print dimension
m1.ndim
#to print size
#m1.itemsize
m2 = np.array([[1,2],[4,5],[5,6]],dtype=np.float32)
m2.itemsize
print(m2)
#to print size of array
m2.size


# In[ ]:




# In[14]:

#to print shape
s = np.array([[9,2],[4,10],[8,6]])
s.shape
#changing shape
s.reshape(2,3)
#flatten array
s.ravel()


# In[18]:

op = np.array([[1,2],[4,5],[8,6]])
#op.min()
#op.max()
#sum column wise
op.sum(axis = 0)
#sum row-wise
op.sum(axis = 1)
#square root
np.sqrt(op)
#sd
np.std(op)

            


# # basic maths operation

# In[21]:

mat = np.array([[1,2],[4,5]])
mat1 = np.array([[11,12],[8,6]])
#addition
mat+mat1
#matrix mul
mat.dot(mat1)


# In[47]:

#complex number
cc  = np.array([[1,2],[4,5],[5,6]],dtype = complex)
cc
#intialize with placeholder number
np.zeros((3,4))
np.ones((2,2))
#creating array with range
np.arange(1,5,2)
#creating numbers in between the specified range
np.linspace(1,5,10)


# # indexing and slicing

# In[31]:

#slicing
sl = np.array([6,7,8])
sl[0:2]
sl[-1]
#multi dimensional array
slm = np.array([[4,3,2],[5,6,7],[12,44,33]])
slm
#slm[1,2]
slm[0:2,2]
#last(rows,colms)
slm[-1]
slm[-1,0:2]
#going through all the rows
slm[:,1:3]


# In[64]:

#indexing with boolean arrays
bo = np.arange(12).reshape(3,4)
#bo
com = bo<5
com



# In[35]:

#iteration
it= np.array([[4,3,2],[5,6,7],[12,44,33]])
for row in it:
    print(row)
#flatten array and iterate
for cell in it.flat:
    print(cell)


# # stacking and splitting

# In[40]:

st = np.arange(6).reshape(3,2)
st1 = np.arange(6,12).reshape(3,2)
#st
#st1
#stacking horizontally
np.vstack((st,st1))
#stacking vertically
np.hstack((st1,st))


# In[47]:

#slicing
st1 = np.arange(30).reshape(2,15)
#st1
#horizontally
res = np.hsplit(st1,3)
res[2]
#vertically
result = np.vsplit(st1,2)
result[0]

