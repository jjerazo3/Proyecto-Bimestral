#!/usr/bin/env python
# coding: utf-8

# In[5]:


suma = 0
n = 0
j=0
print('Ingrese diferentes enteros: ')
while (suma < 10000):
    j = int(input())
    if j == 0:
        print('El numero tiene que ser mayor a 0.')
    elif j > 10000:
        print('El numero tiene que ser menor a 10000')
    suma = j + suma
    n +=1

media = suma / n
print(f'Ingresaste {n} números.')
print(f'La media es: ', media)
print(f'La suma de los valores ingresados es: ', suma) 


# In[ ]:





# In[ ]:




