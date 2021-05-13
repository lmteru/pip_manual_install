#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pip


# In[26]:


def install(pack_name):
    if hasattr(pip, 'main'):
        pip.main(['install', pack_name])
    else:
        pip._internal.main(['install', package])


# In[27]:


f = open("requirements.txt", "r")
req = f.read().splitlines()

print(r)
f.close()


# In[28]:


for r in req:
    install(r)


# In[ ]:


