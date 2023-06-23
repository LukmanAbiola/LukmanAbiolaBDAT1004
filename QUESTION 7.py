#!/usr/bin/env python
# coding: utf-8

# In[1]:


## File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.
## Write a function bldcount() that reads the file with name name and reports (i.e.,
## prints) how many patients there are in each bloodtype.
## >>> bldcount('bloodtype.txt')
## There are 10 patients of blood type A.
## There is one patient of blood type B.
## There are 10 patients of blood type AB.
## There are 12 patients of blood type O.
## There are no patients of blood type OO.


# In[4]:


def bldcount(name):
    blood_types = ["A", "B", "AB", "O", "OO"]
    blood_count = [0, 0, 0, 0, 0]
    with open(name, "r") as f:
        data = f.read()
        patients = data.split()
        for patient in patients:
            for i in range(len(blood_types)):
                if patient == blood_types[i]:
                    blood_count[i] += 1
    for i in range(len(blood_types)):
        if blood_count[i] == 1:  print(f"There is one patient of blood type {blood_types[i]}.")
            elif blood_count[i] > 1:
            print(f"There are {blood_count[i]} patients of blood type {blood_types[i]}.")
        else:
            print(f"There are no patients of blood type {blood_types[i]}.")
        
          


# In[ ]:




