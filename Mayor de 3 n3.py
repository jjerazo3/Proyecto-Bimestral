#!/usr/bin/env python
# coding: utf-8

# In[7]:


n1 = 0
n2 = 0
n3 = 0

print("ingrese 3 enteros diferentes")
n1 = int(input())
n2 = int(input())
n3 = int(input())

if ((n1 > n2) and (n1 > n3)):
    print("El numero mayor es: " +str(n1))
else:
    if ((n2 > n1) and (n2 > n3)):
        print("El numero mayor es: " +str(n2))
    else:
        print("El numero mayor es: " +str(n3))


# In[ ]:





# In[ ]:




