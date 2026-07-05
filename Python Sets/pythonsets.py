"""
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.

"""
myset = {"apple", "banana", "cherry"}
print(myset)

#Duplicates are not allowed hence ignored
myset = {"apple", "banana", "banana", "cherry"}
print(myset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, 0, 2}

print(thisset)

#Get the length using len()
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(len(thisset))