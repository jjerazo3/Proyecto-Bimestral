#!/usr/bin/env python
# coding: utf-8

# In[2]:


lc = 0
at = 0
ar = 0
A = 0
B = 0
D = 0
ats = 0
area = 0
print("Programa que permite el calculo de un poligono")
print("Ingrese el lado del cuadrado")
lc = float(input())
print("Ingrese la altura del triangulo")
at = float(input())
print("Ingrese la altura del rectangulo")
ar = float(input())

A = (lc * lc)
B = (lc * at) / 2
ats = B * 3
D = lc + ar
area = A + ats + D

print("El area del poligono es: " + str(area)+ " Compuesto por un cuadrado de largo " +str(lc)+ " un triangulo de altura " +str(at) + " y un rectangulo de altura: " + str(ar))


# In[ ]:




