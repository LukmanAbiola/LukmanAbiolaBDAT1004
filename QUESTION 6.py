#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pig(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        return word.lower() + 'way'
    else:
        return word[1:].lower() + word[0].lower() + 'ay'


# In[ ]:





# In[ ]:




