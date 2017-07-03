
# coding: utf-8

# In[8]:


#List comprehension

#for i in range(5):

xyz=[i for i in range(5)]
print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)
print(xyz)



    
    
    


# In[10]:


#generators
xyz=[i for i in range(5)]
print(xyz)

xyz=(i for i in range(5))
print(xyz)

for i in xyz:
    print(i)


