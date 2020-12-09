#!/usr/bin/env python
# coding: utf-8

# In[5]:


m = 0
cm = 0
km = 0
ft = 0
ic = 0

print("Programa que permite convertir una cantidad en metros, a centimetros kilometros, pies y pulgadas")

print("Ingrese la cantidad en metros: ")
m = float(input())

cm = m * 100
km = m / 1000
ft = m * 3.28
ic = m * 39.37

print("kilometros: " + str(km) + ", centimetros: " +str(cm) + ", pies: " +str(ft) + " pulgadas: " + str(ic))


# In[ ]:




