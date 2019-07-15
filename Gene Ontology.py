#!/usr/bin/env python
# coding: utf-8

# In[1]:


from goatools import obo_parser


# In[2]:


import wget
import os


# In[3]:


url = 'http://purl.obolibrary.org/obo/go/go-basic.obo'
print("Our Data is taken from %s" % os.getcwd())
folder = os.getcwd() + '/goProjectData'
os.mkdir(folder)
go_obo = wget.download(url,folder+'/go obo file')


# In[4]:


print("File path :" )
print(go_obo)


# In[5]:


goDic = obo_parser.GODag(go_obo)


# In[6]:


id = 'GO:0000001'
track = go[id]
print(track)


# In[9]:


id = 'GO:0000001'
track =goDic[id]
print(track)
print('Go Term Name: {}'.format(track.name))
print('Go Term namespace: {}'.format(track.namespace))
print('Go Term Parents : {}'.format(track.parents))


# In[10]:


for i in track.parents
       print (i)


# In[11]:


for i in track.parents:
    print(i)


# In[ ]:




