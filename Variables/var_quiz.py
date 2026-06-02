#Create a variable x and assign it the value 5
x=5

#Create a variable y and assign it the value "John"
y="John"

#Use the type() function to print the type of x
print(type(x))

#Define a local variable a and assign it the value fantastic and use it locally
a="fantastic"

def myfunc():
    print("Python is "+a)
myfunc()

#Define a local varibale b and assign it the value of awesome and use it globally
b="awesome"
def myfunc():
    global b
    print("Python is "+b)

myfunc()

#define both local and global variables c and d with the values fantastic and awesome and use them locally and globally

c="awesome"
def myfunc():
    d="fantastic"
    print("Python is "+d)
myfunc()
print("Python is "+c)

#change the varibale c to goooood and use it globally
c="awesome"
def myfunc():
    global c
    c="goooood"
    print("Python is "+c)
myfunc()