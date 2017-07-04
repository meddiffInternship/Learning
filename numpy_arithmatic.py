
# coding: utf-8

# In[1]:


import numpy as np


# In[9]:


a=np.array([[1,2],[2,3],[3,2]])
b=np.array([[3,2],[1,5],[6,1]])
print('a is \n{}\n b is \n{}'.format(a,b))


# In[14]:


print('addition of a nd b:\n',a+b)
print('sub of a nd b:\n',a-b)
print('mul of a nd b:\n',a*b)
print('div of a nd b:\n',a/b)


# In[23]:


#matrix product
x=np.array([[1,2],[2,3]])
y=np.array([[3,2],[1,5]])
z=np.array([[0,2],[1,5],[0,1]])
print('dot product :\n',np.dot(x,y))

