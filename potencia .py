#!/usr/bin/env python
# coding: utf-8

# In[4]:


base = 0
pot = 0
cont = 1
resul = 1

print("Ingresar la base de la potencia")
base = float(input())
print("Ingresar la potencia")
pot= float(input())

while cont <= pot :
    resul =- resul * base
    cont = cont + 1
    
print ("La potencia de " + str(base) + " elevado a " + str(pot) + " es: " + str(resul))


# In[ ]:




