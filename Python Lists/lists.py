thisList = ["apple", "banana", "cherry"]
print(thisList)

#List items are ordered, changeable, and allow duplicate values
#List items are indexed, the first item has index [0], the second item has index[1] etc:

#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thisList = ["apple", "banana", "cherry"]
print(len(thisList))

#String items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 3, 5, 7]
list3 = [True, False, True]

#A list can contain different data types
list1 = ["abc", 34, True, "male"]

#Determine the data type list using type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#It is possible to use the list() constructor when creating a new list:
thisList = list(("apple", "banana", "cherry"))
print(thisList)

#Negative Indexing

#Negative indexing means start from the end

#-1 refers to the last item, -2 refers to the second last item etc.
#Example

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
Example

Return the third, fourth, and fifth item:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#By leaving the start value, the range will start at the first item:
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#By leaving out the end value, the range will go on to the end of the list:
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Specify negative indexes if you want to start the search from the end of the list:
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#To determine if a specified item is present in a list use the in keyword:
#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")