#!/usr/bin/env python
# coding: utf-8

# In[3]:


def SeriePrimos(limite1):
    n = 0
    d = 3
    divisor = 1
    suma = 0
    primo = 0
    estado = False

    for k in range(1, limite1 + 1):
        n = n + 1
        while not estado:
            for i in range(1, primo + 1):
                if primo % i == 0:
                    divisor += 1
            if divisor == 2:
                d = primo
                primo += 1
                estado = True
            else:
                primo = primo + 1
                estado = False
            divisor = 0

        if k % 2 == 0:
            suma = suma - (n / d)
            print(f' - {n} / {d}', end=" ")
        else:
            suma = suma + (n / d)
            if k == 1:
                print(f'{n} / {d}', end=" ")
            else:

                print(f' + {n} / {d}', end=" ")

        estado = False
    return suma


limite1 = int(input("Ingrese un límite:"))
print(' = ', SeriePrimos(limite1))


# In[ ]:




