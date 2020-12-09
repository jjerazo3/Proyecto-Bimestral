#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cont=1
cont1=1
n=0
divisor=0
num=0

print("Ingrese el limite de numero a verificar si son primos")

n=int(input())

while cont <= n :
    print("Ingrese el numero a verificar")
    num = int(input())
    
    while cont1 <= num :
        if num % cont1 == 0 :
            divisor = divisor + 1
        cont1 = cont1 + 1 
    if divisor == 2 :
        print(str(num) + " es primo")
        print("---------")
    else :
        print (str(num) + " no es primo")
    
    cont = 1
    divisor = 0
    cont = cont + 1
    


# In[ ]:




