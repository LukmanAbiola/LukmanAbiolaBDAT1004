#!/usr/bin/env python
# coding: utf-8

# In[2]:


## A  Trying to add incompatible variables, as in adding 6 + ‘a’


# In[4]:


6 + 'a'


# In[5]:


## B Referring to the 12th item of a list that has only 10 items


# In[6]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[11])


# In[7]:


## C Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)


# In[8]:


import math

math.sqrt(-1.0)


# In[9]:


## D Using an undeclared variable, such as print(x) when x has not been defined 


# In[10]:


print(x)


# In[11]:


## E Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.


# In[13]:


filename = "getmelit.txt"
with open(filename) as file:
    content = file.read()


# In[ ]:




