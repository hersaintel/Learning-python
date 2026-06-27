#You can use the built-in list method copy() to copy a list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to create a copy is using the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#You can also make a copy of a list by using the : operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)