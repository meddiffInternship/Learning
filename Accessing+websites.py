
# coding: utf-8

# # Accessing websites

# In[1]:

import urllib.request
import urllib.parse
import re


# In[3]:

#getting source code of website
url = urllib.request.urlopen('http://www.auntminnie.com/')
print(url.read())


# In[ ]:

try:
    url = urllib.request.urlopen("http://www.google.com/search?q=test")
    print(url.read())
except Exception as e:
    print(str(e))


# In[83]:

url = 'http://www.auntminnie.com/'
values = {'sec':'def'}
data = urllib.parse.urlencode(values)
data = data.encode('UTF-8')
reqst = urllib.request.Request(url,data)
resp = urllib.request.urlopen(reqst)
respData = resp.read()
#print(respData)

paragraph = re.escape(r'<meta>(.?*)</meta>',str(respData))
for para in paragraph:
    print(para)


# In[67]:




# # Regular Expression

# In[30]:

import re
import csv


# In[60]:

#testing
file = open("/home/aayushi/Desktop/aunt.csv",'r').read()
#print(file)
word = re.findall(r'[A-z][a-z]*\s\d[0-9].\s[0-9]*',file)
medical_term =re.search(r'r[a-y]*',file,flags = 0)
#print(word)
print(medical_term)


# In[56]:

x = 0
medical_term_dict = {}
for words in len(file) :
    medical_term_dict[words] = medical_term[x]
    x+=1
print(medical_term_dict)
    
    

