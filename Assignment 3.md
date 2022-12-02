# Q1. Why are functions advantageous to have in your programs?

Answer:-

Functions are advantageous as they make the code repeatable, i.e we can store a code inside a function and use the function whenever required without writing it again.
Whenever we have a requirement where we need to use the same peace of 
code multiple times than instead if writing it multiple times, function can be created.



# Q2. When does the code in a function run: when it&#39;s specified or when it&#39;s called?

Answer:-

Code in the function execute when it is called.



# Q3.What statement creates a function?

Answer:-

def keyword is used to create the function.  
  
e.g.
def test():  
    print("sample function")  
    
So, here we are defining the function test using def keyword and then the function name followed by brackets.



# Q4.What is the difference between a function and a function call?

Answer-
Function is used to create to increase the reusability of the piece of code. Suppose a set of code is required to be executed
at various places inside a program then instead of writing same piece of code multiple times, function can be created for it.

And whenever required to execute that piece of code, function can be called by using the name followed by brackets and pass the
arguments if present.



# Q5. How many global scopes are there in a Python program? How many local scopes?

Answer:-

There is only one global scope in python program. SO, if a variable is declared in global scope it remain available throughout
the program.

Local scope can be any in python program. If a variable is defined in a function then it can be accessed only within that function and cannot be used outside that program.

Now same variable name can be defined inside different functions and so those has scope inside only those functions.

Also same variable name can be of global scope and local scope and so its usage.


# Q6.What happens to variables in a local scope when the function call returns?

Answer:-

Local variable scope is limited to the funnction in which it is defined. So it is not accessible outside the function and it is destroyed
once the control comes out of fucntion.

# Q7.What is the concept of a return value? Is it possible to have a return value in an expression?

Answer:-

When we define a function to process some data , sometimes it is expected to get the result from the function and then further
processing is required based on the result of the function. Since the local variables cannot be accessed outside the function
so return statement is used. It is used to pass the result of the function to the calling place.

yes return value can be used in expression. e.g. if a function is doing some computation and returns a number than it can be used as below-



```python

def func1():
    return 10
    
a = func1() * 10

print(a)
```

    100
    

# Q8. If a function does not have a return statement, what is the return value of a call to that function?

Answer:-

If a function does not have a return statement then it returns None.

# Q9. How do you make a function variable refer to the global variable?

Answer:-

Variable name should be preceded by global keyword to make the varibale as global variable.  
e.g. global a = 10

# Q10. What is the data type of None?

Answer:-

Data type of None is NoneType

# Q11 What does the sentence import areallyourpetsnamederic do?

Answer:-

Import statement is used to import the existing module in current code. Since the modules are already prepared by someone with a functionality and we want to use same functionality in our code we can use import statement to import into our code.

So, here import areallyourpetsnamederic is used to import the functionalities present in areallyourpetsnamederic module to our code and use the functions/varibales present in this in our logic.


# Q12.If you had a bacon() feature in a spam module, what would you call it after importing spam?

Answer:-

we need to use the statement spam.bacon() to use this function in our code

# Q13. What can you do to save a programme from crashing if it encounters an error?

Answer:-

To save a program from crashing we can put the code in try except block and catch the exception and do a proper exception handling.

Generally if there are certain conditions where the program can crash then that piece of code can be present in try block
and except block can be written to handle the different exceptions which can be thrown by code present in try block.



# Q14.What is the purpose of the try clause? What is the purpose of the except clause?

Answer:-

Try clause is used to contain a piece of a code which can throw error during execution. 
if we do not use try block then program can terminate abnormally which can result in data or files in error state. 
so proper error handling can be done by putting the code in try block

except clause is used to catch the exceptions which can be thrown by the code in try block. We can mention differnt type of exceptions
in except clause and can gracefully terminate the code


```python

```
