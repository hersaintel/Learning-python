"""
You can return a range of characters by using the slice syntax
specify the start index, separated by a colon, to return a part of the string.
"""
#Example
#Get the characters from position 2 to position 5:

b = "Hello,World!"
print(b[2:5])

#Slice from the beginning
b = "Hello, world!"
print(b[:5])

#Slice to the end
txt = "Hello, world!"
b = txt[2:]
print(b)


#Negative Indexing
#Use negative indexes to start the slice from the end of the string: 
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])