#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print &quot;Hello Python&quot;?

# In[1]:


print("Hello Python")


# # 2. Write a Python program to do arithmetical operations addition and division.?

# In[2]:


a = 31
b = 3


# In[4]:


# Addition Operation
c = a+b
print(c)


# In[5]:


# Division Operation
d = a/b
print(d)


# # 3. Write a Python program to find the area of a triangle?
Formula for area of triangle is 0.5*base*height
# In[18]:


base = int(input("Enter length of base: "))
height = int(input("Enter length of height: "))

area = 0.5*base*height

print("Area of the triangle = %d unit square" %area)


# # 4. Write a Python program to swap two variables?

# In[29]:


# let the two variables be a,b
a = 10
b = 21

print("\nvalues before swapping are a = %d, b = %d\n" % (a,b))
#swapping values of a and b using another variable, lets say temp

temp = a
a = b
b = temp

print("Values after swapping are a = %d, b = %d" %(a, b))


# # 5. Write a Python program to generate a random number?

# In[40]:


import random
print(random.randint(0,50))

