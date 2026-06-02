#Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Many values to multiple variables
x,y,z="Bananas","Oranges","Apples"
print(x)
print(y)
print(z)

#One value to multiple variables
x=y=z="Apples"
print(x)
print(y)
print(z)

#Unpacking a collection
fruits=["Oranges","Apples","bananas"]
x,y,z=fruits
print(x)
print(y)
print(z)

#The print() function is used to output variables
x=("Python is good!")
print(x)

x=3
y=4
print(x+y)

x=5
y="John"
print(x,y)

#Global variables (a)create a variable outside a function and use it inside a function
x="awesome"
def myfunc():
    print("Python is " + x)
myfunc()
#(b)create a variable inside a function with the same name as the global variable
x="awesome"
def myfunc():
    x="fantastic"
    print("Python is "+x)
myfunc()

print("Python is "+x)

#If you create a global variable inside a function, the variable belongs to the global scope. To create a global variable use global
def myfunc():
    global x
    x="awesome"
    print("Python is "+x)
myfunc()

#Also use the global keyword if you want to change a global variable inside a function
x="awesome"

def myfunc():
    global x
    x="fantastic"
    print("Python is "+x)

myfunc()