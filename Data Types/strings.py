#Strings in python are either surrounded by single quotation marks or double.
print("Hello")
print('Hello')

#You can use quotes inside a string as long as they don't match the quotes surrounding the string
print("It's a good day")
print('He is called "John"')

#Assign string to a variable.
x = 'Hello'
print(x)

#Multi-line strings 
#You can assign a multiline string to a variable using three quotes
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""#or use single quotes
print(x)

"""
Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
#Loop through the letters in the word banana.
for x in "banana":
    print(x)

#To get the length of a string use the len() function
a = ("Hello")
print(len(a))

#To check if a certain character or word is present in a string use the keyword in
txt = 'check if a certain character or word is present'
print('check' in txt)

#use the if statement
txt = 'check if a certain character or word is present'
if 'check' in txt:
    print("Yes 'check' is present")

#To check if a certain character or phrase is not present in a string we use the keyword not in
txt = 'check if a certain character or word is present'
print('book'not in txt )

#use it in an if statement
txt = 'check if a certain character or word is present'
if 'book' not in txt:
    print("No 'book' is not present")
