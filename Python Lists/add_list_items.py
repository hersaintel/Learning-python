#Append items
#To add an item at the end of alist use the append() method
thislist = ["apple", "banana"]
thislist.append("orange")
print(thislist)

#To insert a list item at a specified index use the insert() method
thislist = ["banana", "orange"]
thislist.insert(1, "apple")
print(thislist)

#To append elements of another list to the current list use the extend() method
thislist = ["banana", "apple"]
list = ["cherry", "mango"]
thislist.extend(list)
print(thislist)

#The extend() method does not have to append lists only, you can add any iterable object (tuples, sets, dictionaries etc)
thislist = ["mango", "cherry"]
thistuple = ("range", "rover")
thislist.extend(thistuple)
print(thislist)