
# coding: utf-8

# In[8]:


#concatinating using join

names = ['indu' , 'yash' , 'pooja']

#for name in names:
    #print('hello there ,' +name)
    #print(''.join(['hello there, ',name]))
    
print(', '.join(names)) 


# In[10]:


#
import os

location_os_files = 'D:\\Internship\\python\\tinker'

file_name = 'tinker.py'

print(location_os_files + '\\' + file_name)

with open(os.path.join(location_os_files, file_name)) as f:
    print(f.read)


# In[14]:


#string formatting

who = 'Indu'

how_many = 12

print('{1} bought {0} apples today'.format(who,how_many))


