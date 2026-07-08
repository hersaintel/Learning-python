#To remove an item in a set use the remove() or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"applae", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#The del keyword will delete the set completely
thisset = {"apple", "banana"}
del thisset