#!/usr/bin/env python
# coding: utf-8

# In[3]:



serieLenght = int(input("Ingrese el limite de la serie Fibonacci: "))
n = 1
primero = 0
segundo = 1
if serieLenght % 2 == 0:
    print(int(serieLenght/2))
    for n in range(n, int(serieLenght/2)+n):
        print(primero)
        print(segundo)
        primero = primero + segundo
        segundo = primero + segundo
else:
    n = n - 2
    print(primero)
    primero = 1

    for n in range(int(n + serieLenght/2), int(serieLenght)-2):
        print(primero)
        print(segundo)
        primero = primero + segundo
        segundo = primero + segundo


# In[ ]:




