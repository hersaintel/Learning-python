#the remove() method is used to remove an item
thislist = ["banana", "apple", "mango"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The clear() method clears the list but the list remains:

thislist = ["banana", "cherry"]
thislist.clear()
print(thislist)