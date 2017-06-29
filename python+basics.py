
# coding: utf-8

# # python basics

# In[ ]:




# # single line argument

# In[ ]:

# print('hey!')
print('hey')


# # mathematical operations

# In[ ]:

6**7 #this expression gives six raised to power 7


# In[ ]:

5/2 #the division in python3 can give result in floating point 


# In[ ]:

3+1


# # variables concept

# In[ ]:

var = 55+34
print(var)


# In[ ]:

var1 = print('whoaa!!')


# In[ ]:

x,y = (3,5)
print(x,y)


# # loop concepts

# In[ ]:

count = 1
while count < 10:
    print(count)
    count +=1


# In[ ]:

number = [23,45,67,89,123,345]
for no in number:
    print(no)
    print('continue ')


# In[ ]:

for number in range(1,20):
    print(number)


# In[ ]:

a = 10
b = 15
c = 9
if (a>b) and (a>c):
    print('a is greater')
elif (b>c) and (b>a):
    print('b is greater')
else:
    print('c is greater')



# # user input 

# In[ ]:

name = input('whats ur age')
print('hello',name)


# # classes 

# In[ ]:

class calculator:
  def add(a,b):
    answer = a+b
    return answer
  def subtract(a,b):
     answer = a-b
     return answer
calculator.add(5,3)


# # list vs tuples

# In[ ]:

tup = (5,4,4,2,3,4)
print(tup)


# # list manipulations

# In[ ]:

lst = [7,7,2,3,90,45,67,23,46759]
lst.append(89)
lst.insert(5,50)
lst.remove(46759)
print(lst.index(2))
print(lst.count(7))
print(lst[2:6])
print(lst[-4])
lst.sort()
print(lst)


# # multidimensional lists

# In[ ]:

lst=[[[12,24],[8,16]],[9,18],[10,20]]
print(lst[-3])
print(lst)


# 

# # multiline printing

# In[ ]:

print(''' this is an example of simple multiline printing

-----------
|         |
|         |
-----------
''')


# # Dictionaries

# In[ ]:

#creating dictionary
fruits ={"watermelon":18,"papaya":24,"litchi":100,"mausambi":55}
print(fruits)
#mutating dictionary
fruits["papaya"] = 20
print(fruits)
#removing a key
del fruits["litchi"]
print(fruits)
#checking length
print (len(fruits))
#checking key is presented in the dictionary"(in)"
for item in fruits:
    if "litchi" in fruits:
        print("found")
    else:
        print("not found")
#printing specified value
print(fruits.get("watermelon","none"))
#printing all values in dictionary
print("*"*5)
print("fruits with cost:")
print("*"*5)
for fruit in fruits:
    print(fruits)
#print all key-value pair
for key,val in fruits.items():
    print(key,val)
#getting keys from specified dictionaries
cost = fruits.keys()
print(cost)
print("the fruits are", "".join(fruits))
print("the fruits are","",fruits.keys())
#print values
for costs in fruits:
    cost = fruits[costs]
    print(cost)
#sorting dictionary
for key,val in sorted(fruits.items()):
    print(key,val)
#adding new value to dictionary
fruits.update({"cherry":90})
print(fruits)

    


# # functions

# In[15]:

def sum(a,b):
    c = a+b
    print(c)
def main():
    sum(5,6)
main()


# # modules examples

# In[ ]:

import sys


# In[ ]:

sys.stderr.write('module accepted')
sys.stderr.flush()
sys.stdout.write('standard output')
print(sys.argv)


# In[ ]:

#if len(sys.argv) > 1:
#print(float(sys.argv[1])+5)
def main(arg):
print(arg)
main(sys.argv[1])())


# # sub process

# In[10]:

import subprocess


# In[12]:

subprocess.call('ls',shell = True)
output = subprocess.check_output('ls',shell = True)
print(output)


# # threading
# 

# In[4]:

import threading
from queue import Queue
import time


# In[7]:

print_lock = threading.Lock()
def example_job(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name,worker)
def threader():
            while True:
                worker = q.get()
                example_job(worker)
                q.task_done()
q = Queue()
for x in range(10):
     t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took:',time.time() - start)


# # String formatting

# In[19]:

names = ['indu','akshay','anupama','trafalgar law','aayushi','abhishek']
for name in names:
    #print('hi'+" " +name)
    print("".join(name))
    


# In[20]:

import os


# In[21]:

location = '/home/aayushi/Desktop/assignment-1'
file_name = 'count.py'
with open(os.path.join(location,file_name)) as f:
    print(f.read())


# In[27]:

who = 'mother'
whom = ' Indu'


# In[28]:

print('{} scolded {} today'.format(who,whom))


# # 
