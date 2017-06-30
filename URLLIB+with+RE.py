
# coding: utf-8

# In[11]:


import urllib.request
import urllib.parse
import re

url = 'https://pythonprogramming.net'
values = {'s':'basics','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(str(respData))

paragraphs = re.findall(r'(P[a-z]*)',str(respData))

for eachP in paragraphs:
    print(eachP)

