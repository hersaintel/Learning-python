"""
There are three numeric types in python

    int
    float
    complex

"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Example

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Example

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) 

#Float can also be scientific numbers with 'e' to indicate the power of 10
#Example

x = 847e6
y = 2E4
z = -6774893e7893

print(type(x))
print(type(y))
print(type(z))

#Complex are numbers written with 'j' as the imaginary part
#Example

x = 9+7j
y = 579j
z = -74893j

print(type(x))
print(type(y))
print(type(z))

#You can convert from one type to another using int(), float() and complex() methods
x = 6    #int
y = 48.9 #float
z = -8j  #Complex

#convert int to float
a = float(x)

#convert float to complex
b = complex(y)

#convert float to int
c = int(y)

#convert int to complex
d = complex(x)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Note: You cannot convert complex numbers into another number type.

#Python does not have a random() function to make random numbers but has a built-in random module to make random numbers

import random

print(random.randrange(1,10))