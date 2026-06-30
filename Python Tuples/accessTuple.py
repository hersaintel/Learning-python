#You can access tuple items by referring to the index number, inside square brackets:
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])

#Negative indexing means start from the end.
#-1 refers to the last item, -2 refers to the second last item etc.
tuple1 = ("apple", "banana", "cherry")
print(tuple1[-1])

"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.
"""
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Check if item i available in a tuple:
thistuple = ("banana", "banana", "cherry")
if "apple" in thistuple:
    print("Yes 'apple' is in thistuple")