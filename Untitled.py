#!/usr/bin/env python
# coding: utf-8

# In[3]:


h24=0
m24=0
h12=0
m12=0
periodo="a.m."

print("Programa para convertir las horas en formato de 24h a formato de 12h")

print("Ingrese la hora en formato 24h")
h24=int(input())
print("Ingrese los minutos")
m24=int(input())

if((h24 < 25) and (h24 >= 0)):
    if (((h24 <= 24) and (h24 >= 0)) and ((m24 >= 0) and (m24 <= 60))) :
        if(m24 == 60):
            h24 = h24 + 1
            m24 = 0
        
        else:
            m12=m24
        
        if(h24 >= h12) :
            if(h24 == 12):
                h12 = h24 - 12
            
            periodo = "p.m."
        
        print("Este tiempo es equivalente a: " +str(h12) + " horas y " +str(m12) + " minutos " + str(periodo))
    

else :
    if(h24 == 0) :
        h12 = h24
        if (m24 == 60) :
            h12 = h12 + 1
            m24 = 0
        
        else :
            m12 = m24
        
        print("Este tiempo es equivalente a: " +str(h12) + " horas y " +str(m12) + " minutos " + str(periodo))
    


# In[ ]:





# In[ ]:




