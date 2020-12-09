#!/usr/bin/env python
# coding: utf-8

# In[2]:


cont=1
n=1
num=0
sumPar=0
sumImpar=0
sumNeg=0
sumPos=0

print("Ingrese el limite de numeros a verificar")
n = int(input())

while cont <= n :
    print ("Ingrese el numero a verificar")
    num = int(input())
    
    if num % 2 == 0 :
        sumPar = sumPar + num
    else :
        sumImpar = sumImpar + num
    if num > 0 :
        sumPos= sumPos + num
    else :
        sumNeg = sumNeg + num 
    cont = cont + 1
    print("La suma de los pares es: " + str(sumPar))
    print("La suma de los impares es: " + str(sumImpar))
    print("La suma de los positivos es: " + str(sumPos))
    print("La suma de los negativos es: " + str(sumNeg))


# In[ ]:




