
# coding: utf-8

# In[1]:

import nltk
import math
import string
from collections import Counter
import os
import glob
from string import digits
from math import log
from pandas import DataFrame
import pandas as pd
import numpy
import re
from textblob import TextBlob


# In[2]:

#from nltk.corpus import stopwords
from nltk.stem import *
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix


# In[3]:

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic('matplotlib inline')


# In[4]:

with open('/home/aayushi/english.txt','r') as sw:
    stopwords = sw.read().splitlines()


# In[5]:

def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove numbers
    3. Remove all stopwords
    4. Returns a list of the cleaned text
    """
    
    result = [i for i in mess if not i.isdigit()]
    
    # Check characters to see if they are in punctuation
    nopunc = [char for char in result if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords]


# In[6]:

def split_into_lemmas(message):
    message = str(message).lower()
    words = TextBlob(message).words
    # for each word, take its "base form" = lemma 
    return [word.lemma for word in words]

#messages.message.head().apply(split_into_lemmas)
#corpus.head().apply(split_into_lemmas)


# In[7]:

def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r')
        a_list.append(f.read())
    f.close()
    return a_list


# In[8]:

mri_var = init_lists('/home/aayushi/Downloads/reports/mri/')
xray_var = init_lists('/home/aayushi/Downloads/reports/x-ray/')


# In[9]:

all_docs = [(i, 'mri') for i in mri_var]
all_docs += [(i, 'xray') for i in xray_var]


# In[10]:

print(len(all_docs))


# In[11]:

corpus = pd.DataFrame(all_docs, columns=['contents', 'labels'])


# In[12]:

#Shuffle the code
corpus = corpus.reindex(numpy.random.permutation(corpus.index))
corpus.head()


# In[13]:

corpus_lemma = pd.DataFrame(all_docs, columns=['contents', 'labels'])


# In[14]:

corpus.head()


# In[15]:

corpus.describe()


# In[16]:

corpus.groupby('labels').describe()


# In[50]:

corpus['length']=corpus['contents'].apply(len)


# In[19]:

corpus.length.describe()


# In[21]:

corpus.head()


# In[22]:

bow_transformer = CountVectorizer(analyzer=split_into_lemmas).fit(corpus['contents'])

# Print total number of vocabulary words
print (len(bow_transformer.vocabulary_))


# In[23]:

print(bow_transformer.vocabulary_)


# In[24]:

content_4 = corpus['contents'][4]
print (content_4)


# In[25]:

print(len(content_4))


# In[26]:

#vector representation of the same content_3
bow4 = bow_transformer.transform([content_4])
print(bow4)
print (bow4.shape)


# In[27]:

print(bow_transformer.get_feature_names()[486])


# In[28]:

corpus_bow = bow_transformer.transform(corpus['contents'])


# In[29]:

corpus_bow


# In[30]:

print('Shape of Sparse Matrix: ', corpus_bow.shape)
print('Amount of Non-Zero occurences: ', corpus_bow.nnz)


# In[31]:

sparsity = (100.0 * corpus_bow.nnz / (corpus_bow.shape[0] * corpus_bow.shape[1]))
print('sparsity: {}'.format(round(sparsity)))


# In[32]:

#TF-IDF
tfidf_transformer = TfidfTransformer().fit(corpus_bow)


# In[33]:

tfidf4 = tfidf_transformer.transform(bow4)
print(tfidf4)


# In[34]:

print(tfidf_transformer.idf_[bow_transformer.vocabulary_['spine']])


# In[35]:

# Corpus transformation
corpus_tfidf = tfidf_transformer.transform(corpus_bow)
print(corpus_tfidf.shape)


# In[36]:

print(corpus_tfidf)


# In[37]:

#Building a model

doc_train, doc_test, label_train, label_test = train_test_split(corpus['contents'], corpus['labels'], test_size=0.3)


# In[38]:

print ('The training size is 70% of the entire dataset. Size of Training Set: ', len(doc_train))
print ('The test size is 30% of the entire dataset. Size of Test Set:         ', len(doc_test))
print ('Total Size of the dataset:                                            ', len(doc_train) + len(doc_test))


# In[39]:

#Creating a Data Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=split_into_lemmas)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])


# In[40]:

pipeline.fit(doc_train,label_train)


# In[51]:

predictions = pipeline.predict(doc_train)


# In[52]:

print('predicted:', pipeline.predict(tfidf4)[0])


# In[43]:

print(len(predictions))


# In[44]:

print ('accuracy', accuracy_score(label_train,predictions))
print ('confusion matrix\n', confusion_matrix(label_train,predictions))
print ('(row=expected, col=predicted)')


# In[45]:

print (classification_report(predictions,label_train))


# In[46]:

#For Test Set
pipeline.fit(doc_test,label_test)
predictions_testset = pipeline.predict(doc_test)
print(len(predictions_testset))
print ('accuracy', accuracy_score(label_test,predictions_testset))
print ('confusion matrix\n', confusion_matrix(label_test,predictions_testset))
print ('(row=expected, col=predicted)')


# In[47]:

print (classification_report(predictions_testset,label_test))

