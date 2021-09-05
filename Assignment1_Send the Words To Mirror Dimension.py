#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program that accepts a word from the user and reverse it.



Sample Test Case



Input : Edyoda

output: adoydE


# In[9]:


string1= input("Input a word to reverse: ")
for i in range(len(word) - 1, -1, -1):
    print(string1[i], end="")


# In[ ]:




