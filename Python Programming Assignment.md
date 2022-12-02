# 1. Write a Python program to print &quot;Hello Python&quot;?


```python
print("Hello Python")
```

    Hello Python
    

# 2. Write a Python program to do arithmetical operations addition and division.?


```python
a = 31
b = 3
```


```python
# Addition Operation
c = a+b
print(c)
```

    34
    


```python
# Division Operation
d = a/b
print(d)
```

    10.333333333333334
    

# 3. Write a Python program to find the area of a triangle?
Formula for area of triangle is 0.5*base*height

```python
base = int(input("Enter length of base: "))
height = int(input("Enter length of height: "))

area = 0.5*base*height

print("Area of the triangle = %d unit square" %area)
```

    Enter length of base: 35
    Enter length of height: 76
    Area of the triangle = 1330 unit square
    

# 4. Write a Python program to swap two variables?


```python
# let the two variables be a,b
a = 10
b = 21

print("\nvalues before swapping are a = %d, b = %d\n" % (a,b))
#swapping values of a and b using another variable, lets say temp

temp = a
a = b
b = temp

print("Values after swapping are a = %d, b = %d" %(a, b))
```

    
    values before swapping are a = 10, b = 21
    
    Values after swapping are a = 21, b = 10
    

# 5. Write a Python program to generate a random number?


```python
import random
print(random.randint(0,50))
```

    26
    
