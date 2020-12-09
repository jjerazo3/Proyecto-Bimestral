#!/usr/bin/env python
# coding: utf-8

# In[1]:


gc=0
gf=0
gk=0

print("Programa para convertir de grados Centigrados a grados Kelvin y Farenheit")

print("Ingrese los grados Centigrados")
gc=float(input())

gf = (gc * 9/5) + 32
gk = gc + 273.15

print("La equivalencia a grados F es: " + str(gf))
print("La equivalencia a grados K es: " + str(gk))


# In[ ]:




