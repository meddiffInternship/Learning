
# coding: utf-8

# In[12]:


import pandas as pd
import datetime
#import pandas.io.data as web
from pandas_datareader import data as web


# In[17]:


df=pd.read_excel('E:\\indu\\python\\pandas\\pandas.xlsx')
df


# In[24]:


print(df['CGPA'].max())
print(df['CGPA'].min())
print(df['CGPA'].mean())


# In[22]:


print(df['Name'][df['Branch']=='msw'])


# In[26]:


df.shape


# In[34]:


rows, column=df.shape
print(rows)
print(column)


# In[35]:


df.head()


# In[36]:


print(df.tail(5))


# In[37]:


print(df[2:5])


# In[38]:


df.describe()

