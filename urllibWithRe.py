
# coding: utf-8

# In[2]:


import urllib.request
import urllib.parse
import re


# In[11]:


url='http://pythonprogramming.net'
values={'s':'basic','submit':'search'}
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()
para=re.findall(r'<p>(.*?)</p>',str(respData))
for eachp in para:
    print(eachp)


# In[ ]:




