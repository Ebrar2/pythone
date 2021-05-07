#!/usr/bin/env python
# coding: utf-8

# In[100]:


def temizle(x):
    y=len(x)
    a=0
    z=[]
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


# In[101]:


b="Ah5me4t"
i="M9eHm4eT"
u="Ha3K5a1n"
x=temizle(b)
#print(x)
y=temizle(i)
#print(y)
z=temizle(u)
#print(z)
liste=[x,y,z]
print(liste)


# In[ ]:




