
# coding: utf-8

# In[22]:


def add(n1,n2=5):
    print(n1,n2)
    
add(1)


# In[32]:


x=6

def simple():
    globx=x
    print(x)
    globx +=5
    print(globx)
    return globx
    
simple()


# In[ ]:


text='i love python\n Its intresting'

savefile=open('D:\\Internship\\python\\Text.txt','w')
savefile.write(text)
savefile.close()


# In[ ]:


Append='\nINDU'
appendfile=open('D:\\Internship\\python\\Text.txt','a')
appendfile.write(Append)
appendfile.close()


# In[ ]:


#to read a file
readme=open('D:\\Internship\\python\\Text.txt','r').read()
print(readme)


# In[49]:


#class

class calc:
    def add(x,y):
        return x+y
    
    def sub(x,y):
        return x-y
    
    def mul(x,y):
        return x*y
    
    def div(x,y):
        return x/y
    
    
calc.div(1,2)
        


# In[53]:


def epic():
       print("woow this is great")
       
if __name__ == '__main__':
   print('such a great module')
   
#epic()
   
   


# In[66]:


x=input('what is your name? ')

print("hello",x)


# In[64]:


import statistics as s

example_list=[1,2,4,5,7,3,1,3,2,1]

#x=statistics.mean(example_list)
#x=statistics.median(example_list)
#x=statistics.stdev(example_list)
x=s.variance(example_list)
print(x)



# In[88]:


x=(1,2,3,4,5)
y=[2,4,6,8]

def ex():
    return 15,6

#x,y=ex() 
#print(x[1],y[3])
#x[2]=10
y[2]=10
#print(x[2],y[2])
#print(y)

i=0
while i<len(y):
    print(y[i])
    
    i+=1
    


# In[94]:


x=[5,6,2,1,6,7,2,2,2,1]

#x.insert(2,'indu')
#print(x.count(2))
x.sort()
print(x)


# In[100]:


x=[[[5,6],[7,2]],[3,4],[3,7]]
print(x[0][1])


# In[107]:


import csv

with open('D:\\Internship\\python\\CSV\\example.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=",")
    #print(readcsv)
    
    for row in readcsv:
        print(row)
        print(row[0])


# In[109]:


#multiline print

print('''
I
love hogwarts.
Doby is my friend
My wand is super cool
==========
|
|
|



==========

'''

)


# In[124]:


ex={'indu':[23,'blond'],'yash':[23,'black'],'akshi':[10,'brown']}
print(ex['indu'][1])

#ex['poo']=24
print(ex)
#ex['poo']=89
print(ex)


# In[127]:


ex1=-5
ex2=5

print(abs(ex1))

if abs(ex1)==ex2:
    print('hi')


# In[ ]:


import os

curDir = os.getcwd
print(curDir)


# In[ ]:


import time

time.sleep(2)


# In[ ]:


import urllib.request

x = urllib.request.urlopen('https://www.google.com')
print(x.read())


# In[ ]:




