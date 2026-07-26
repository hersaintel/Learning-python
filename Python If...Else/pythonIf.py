"""
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
"""
#If statement:
a = 33
b = 200
if b > a:
    print("b is greater than a")

#Multiple statements in an if block:
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can drink")
    print("You have full legal rights")

#Using a Boolean variable:
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

#Checking if a number is positive:
number = 15
if number > 0:
    print(f"{number} is a positive number")