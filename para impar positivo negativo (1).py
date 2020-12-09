#!/usr/bin/env python
# coding: utf-8

# In[11]:



estado = True
n = []
i = 1
SumaPa = 0
SumaP = 0
SumaI = 0
SumaN = 0

limite = int(input('Ingrese el límite de números que desea verificar: '))
print(f'Ingrese {limite} números para verificar: ')

while estado:
    num = int(input())
    n.append(num)
    if i >= limite:
        estado = False
    i += 1

k = 1
Numbers = list(map(int, n))

for j in range(0, len(n)):
    while k <= n[j]:
        if n[j] % 2 == 0:
            SumaPa = SumaPa + n[j]
        else:
            SumaI = SumaI + n[j]

        if num > 0:
            SumaP = SumaP + n[j]
        else:
            SumaN = SumaN + n[j]
        k += 1

print('La suma de pares es: ', SumaPa)
print('La suma de impares es: ', SumaI)
print('La suma de positivos es: ', SumaP)
print('La suma de negativos es: ', SumaN) 


# In[ ]:




