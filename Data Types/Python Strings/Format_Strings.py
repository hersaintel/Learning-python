"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""
#Create an f-spring
age = 36
txt = f"My name is John, I am {age}"
print(txt) 

#A placeholder can contain variables, operations, functions, and modifiers to format the value
#Add a placehoolder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#A placeholder can contain python code, like math operators
#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59:.2f} dollars"
print(txt)