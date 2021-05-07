#!/usr/bin/env python
# coding: utf-8

# In[5]:


def asal(sayi):
    if(sayi==1):
        return 1
    for y in range(2,sayi):
        if(sayi%y==0):
            return 1


# In[7]:


x=0
while x!=5:
    x=x+1
    sayi=int(input("Sayi:"))
    if asal(sayi)==1:
        print("{} asal degil".format(sayi))
    else:
        print("{} asaldir".format(sayi))


# In[ ]:




