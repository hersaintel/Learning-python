#You can loop through the list items by using a for loop:
#Example: Print all items in the list one by one.

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#You can also loop through the list items by referring to their index number:
#Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


#You can loop through list using a while loop to go through all the index numbers; use the len() function to determine the length of of the list

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#List comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]