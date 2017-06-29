
# coding: utf-8

# # matplot lib 

# In[1]:

from  matplotlib import pyplot as plt


# In[2]:

plt.plot(2,3)
plt.show()


# In[3]:

#line chart
x = [2,3,5,6,7]
y = [9,6,7,8,8]
plt.plot(x,y)
plt.show()


# In[4]:

#labels
plt.title('basic representation')
plt.ylabel('price')
plt.xlabel('litres of petrol')
#plt.plot(x,y)
plt.plot(x,y,'g',linewidth = 8,label = 'line one')
plt.legend()
#grid representation
plt.grid(True, color ='k')
plt.show()


# # matplotlib styles

# In[5]:

x =[4,6,80,23,7,53] 
y = [8,90,66,2,34,56]
plt.scatter(x,y,color = 'c')
plt.title("scatter plot")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


# In[6]:

x1=[23,56,78,10,45]
y1=[70,50,68,90,80]
plt.bar(x,y,color = 'c',align = 'center')
plt.bar(x1,y1,color= 'r')
plt.title("scatter plot")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


# In[7]:

#plotting from csv file
import numpy as np


# In[8]:

x,y =np.loadtxt('/home/aayushi/PSI/samples/bb1.csv',unpack = True, delimiter =',' )
print(x)
print(y)

