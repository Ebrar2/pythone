#!/usr/bin/env python
# coding: utf-8

# In[187]:


def temizle(x):
    y=len(x)
    a=0
    for i in range(0,y):
        if x[i].isdigit()==False and i==0:
            z=x[i].upper()
            d[a]=z
            a=a+1
        elif x[i].isdigit()==False and i!=0:
            z=x[i].lower()
            d[a]=z
            a=a+1
    return d


# In[190]:


b="Ah5me4t"
i="M9eHm4eT"
u="Ha3K5a1n"
x=str(temizle(b))
y=str(temizle(i))
z=str(temizle(u))
liste=x,y,z
print(liste)

