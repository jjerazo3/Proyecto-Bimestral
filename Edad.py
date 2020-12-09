#!/usr/bin/env python
# coding: utf-8

# In[ ]:


an=0
mn=0
dn=0
aa=0
ma=0
da=0
ea=0
em=0
ed=0

print("Ingrese el año de nacimiento:")
an = int(input())
print("Ingrese el mes de nacimiento:")
mn = int(input())
print("Ingrese el dia de nacimiento:")
dn = int(input())
print("Ingrese el año actual:")
aa = int(input())
print("Ingrese el mes actual:")
ma = int(input())
print("Ingrese el dia actual:")
da = int(input())

ea = aa - an
em = ma - mn
ed = da - dn

if (em < 0):
    ea = ea -1
else:
    if ((em == 0) and (ed > 0)) :
        ea = ea -1
if (em < 0):
    em = ma +12 - mn
if (ed < 0):
    ed - da +30 - dn

print("SU eduad actual es: " + str(ea) + " años, " +str(em) + " meses y " + str(ed) + " dias.")


# In[ ]:




