#!/usr/bin/env python
# coding: utf-8

# # 1. What are the two values of the Boolean data type? How do you write them?

# Answer:- Two values for Boolean data types are True and False.
# 
# 

# # 2. What are the three different types of Boolean operators?

# Answer:- Boolean operator is used to check multiple conditions at once. There are 3 types of Boolean operators:
# 1) AND - The expression is true if all the conditions surrounding AND are true   
# 2) OR - The expression is true if any of the condition surrounding OR is true  
# 3) NOT - It is used to negate the result. NOT True becomes False.  
# 
# 

# # 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# Answer -  
#   
# 1) AND-  
# 
# condition1   condition2   condition3   results  
#     0             0          0         False  
#     0             0          1         False  
#     0             1          0         False  
#     0             1          1         False  
#     1             0          0         False  
#     1             0          1         False  
#     1             1          0         False  
#     1             1          1         True  
#       
# 2) OR-  
#   
# condition1   condition2   condition3   results  
#     0             0          0         False  
#     0             0          1         True  
#     0             1          0         True  
#     0             1          1         True  
#     1             0          0         True  
#     1             0          1         True  
#     1             1          0         True  
#     1             1          1         True  
#   
# 3) NOT-  
#   
# condition1   result  
#     True     False  
#     False    True   
#       
#  Note: - Here 0 in the condition means False and 1 in the condition means True  
#  
#  

# # 4. What are the values of the following expressions?
# (5 &gt; 4) and (3 == 5)
# 
# not (5 &gt; 4)
# 
# (5 &gt; 4) or (3 == 5)
# 
# not ((5 &gt; 4) or (3 == 5))
# 
# (True and True) and (True == False)
# 
# (not False) or (not True)
Answer:-

False
False
True
False
False
True


# # 5. What are the six comparison operators?
Answer:-
    
Copmarison operators are as follows:
    
    (>)       - greater than  
    (>=)        - greater than or equal to  
    (<)         - less than  
    (<=)        - less than or equal to  
    (==)        - equal to  
    (!=)        - not equal to  
    
    
# # 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
Answer:-
    
Equal to (==) operator is used to check if two variables,or two conditions are equal.  
Assignment operator (=) is used to assign the value to a variable.  
  
e.g: If we want state if 2 variables(a,b) have same value we will use a == b.
  
    But if we want to assign the value of variable b to variable a , we can use a = b  
  
  
# # 7. Identify the three blocks in this code:
# 
# spam = 0
# 
# if spam == 10: 
# print('eggs')  
# if spam > 5:  
# print('bacon')  
# else:  
# print('ham')  
# print('spam')  
# print('spam')  

# Answer:- 
#     
# Three blocks are:  
#   
# 1) 
# if spam == 10:  
# print('eggs')  
#   
# 2)  
# if spam > 5:    
# print('bacon')  
#   
# 3)  
# else:  
# print('ham')  
# print('spam')  
# print('spam')  
# 
# 

# # 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[1]:


Answer:
    
spam = int(input("Enter any number: " ))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    
    


# # 9.If your programme is stuck in an endless loop, what keys you’ll press?
Answer:-
    
ctrl + c or restart the kernel


# # 10. How can you tell the difference between break and continue?
Answer:-
    
break - It is used to break the current loop and pass control to the next instruction after the loop
continue - It is used to skip the execution  of current iteration of loop and passes control to next iteration


# # 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Answer:-

Though all 3 options will give same output. But there is a difference:

1. range(10): It will by defualt take the first limit as 0, and display 10 values from 0 to 9

2. range(0,10): In this we have specified that first limit is 0, i.e. start the range from 0 to next 10 values. It will also display the same result. But we can set different value to start range from that value.

3. range(0,10,1): In this we have mentioned that start range from 0 to 10 and with an increment of 1. we can keep any increment we want.


# # 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[13]:


a = range(1,11)
for i in a:
    print(i)


# In[16]:


i = 1
while(i <= 10):
    print(i,end='\n')
    i += 1
    
    


# # 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Answer:-
    
We will call it by,
spam.bacon()

