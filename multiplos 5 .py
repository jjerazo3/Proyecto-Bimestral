#!/usr/bin/env python
# coding: utf-8

# In[8]:


l = 100
j = 0
i = 0
print("Ciclo FOR")
for i in range(l+1):
    if i % 5 == 0:
        print(i,end=" " )
print("/n")
print("Ciclo WHILE")

while True:
  if j % 5 == 0:
      print(j,end=" ")
  j+=1
  if j>l:
    break 


# In[ ]:




