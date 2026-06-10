"""
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.
"""
#Example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#When you run a condition in an if statement, python returns True or False:
#Print a message based on whether the condition is true or false:
a = 300
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater that a")


#The bool() function lets you evaluate a value and return true or false in return:
print(bool("Hello"))
print(bool(15))

#Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False: 
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#You can create a function that returns a boolean value:
def myFunction():
    return True

print(myFunction())

#You can evaluate code based on the Boolean answer of a function:
#Print "YES" if the function returns True, else print "NO":
def myFunction():
    return True
if myFunction():
    print("YES")
else:
    print("NO")

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
"""
x = 200
print(isinstance(x, int))